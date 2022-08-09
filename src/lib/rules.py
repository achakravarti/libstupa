from jinja2 import Environment
from typing import Dict, List, Tuple
from lib.error import InvalidOperationError, InvalidPropertyError, NotFoundError
from .db import Db
from .types import Template, TemplateId, TemplateSummary

import sqlite3

class Validate:
    """Helper validation methods for rules."""

    def __init__(self, db: Db):
        """Initialises this validator."""
        self._db = db

    def exists(self, id_: TemplateId):
        """Checks if a template ID exists."""
        id_.validate()
        if self._db.exec(Db.SQL_ID_EXISTS, (id_.value,))[0][0] == 0:
            raise NotFoundError(f'ID {id_} does not exist')

    def active(self, id_: TemplateId):
        """Checks if a template ID is active."""
        id_.validate()
        if self._db.exec(Db.SQL_ID_ACTIVE, (id_.value,))[0][0] == 0:
            raise InvalidOperationError(f'ID {id_} not active')

    def archived(self, id_: TemplateId):
        """Checks if a template ID is archived."""
        id_.validate()
        if self._db.exec(Db.SQL_ID_ARCHIVED, (id_.value,))[0][0] == 0:
            raise InvalidOperationError(f'ID {id_} not archived')

    def unique(self, entity: Template):
        """Checks if a template ID is unique."""
        entity.id_.validate()
        entity.name.validate()
        entity.version.validate()
        res = self._db.exec(
            Db.SQL_ID_FIND, (entity.name.value, entity.version.value))
        if res is None or len(res) == 0:
            return True
        if res[0][0] != entity.id_.value:
            raise InvalidPropertyError(
                f'template {entity.name.value} ({entity.version.value}) already exists')


class Parse:
    """Helper function to parse records into templates."""

    @staticmethod
    def summary(record: Tuple) -> TemplateSummary:
        """Parses a record to a template summary."""
        return TemplateSummary(record[0], record[1], record[2])

    @staticmethod
    def detail(record: Tuple) -> Template:
        """Parses a record to a template."""
        return Template(record[0], record[1], record[2], record[3], record[4])


class Rule:
    """Operation rules."""

    def __init__(self, sample: bool = False):
        self._db = Db(sample)
        self._vd = Validate(self._db)

    def count_active(self) -> int:
        """Returns the count of active templates."""
        return self._db.exec(Db.SQL_COUNT_ACTIVE, None)[0][0]

    def count_archived(self) -> int:
        """Returns the count of archived templates."""
        return self._db.exec(Db.SQL_COUNT_ARCHIVED, None)[0][0]

    def list_active(self) -> List[TemplateSummary]:
        """Returns the list of active templates."""
        res = self._db.exec(Db.SQL_LIST_ACTIVE, None)
        return [Parse.summary(x) for x in res]

    def list_archived(self) -> List[TemplateSummary]:
        """Returns the list of archived templates."""
        res = self._db.exec(Db.SQL_LIST_ARCHIVED, None)
        return [Parse.summary(x) for x in res]

    def load(self, id_: TemplateId) -> Template:
        """Loads an existing template."""
        self._vd.exists(id_)
        return Parse.detail(self._db.exec(Db.SQL_LOAD, id_.serialize())[0])

    def render(self, id_: TemplateId, subs: Dict) -> str:
        """Renders an existing template."""
        entity = self.load(id_)
        return Environment().from_string(entity.content.value).render(subs)

    def create(self, entity: Template):
        """Creates a new template."""
        entity.validate()
        self._vd.unique(entity)
        self._db.exec(
            Db.SQL_CREATE,
            (entity.name.value, entity.version.value, entity.content.value))

    def update(self, entity: Template):
        """Updates an existing template."""
        entity.validate()
        self._vd.unique(entity)
        self._db.exec(Db.SQL_UPDATE, entity.serialize())

    def archive(self, id_: TemplateId):
        """Archives an active template."""
        self._vd.exists(id_)
        self._vd.active(id_)
        self._db.exec(Db.SQL_ARCHIVE, id_.serialize())

    def restore(self, id_: TemplateId):
        """Restores an archived template."""
        self._vd.exists(id_)
        self._vd.archived(id_)
        self._db.exec(Db.SQL_RESTORE, id_.serialize())

    def delete(self, id_: TemplateId):
        """Deletes an archived template."""
        self._vd.exists(id_)
        self._vd.archived(id_)
        self._db.exec(Db.SQL_DELETE, id_.serialize())
