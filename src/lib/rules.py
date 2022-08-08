from jinja2 import Environment
from typing import Dict, List, Tuple
from lib.error import InvalidOperationError, InvalidPropertyError, NotFoundError
from .db import Db
from .types import Template, TemplateId, TemplateSummary

import sqlite3

class Validate:
    """Helper validation methods for rules."""

    @staticmethod
    def exists(id_: TemplateId):
        """Checks if a template ID exists."""
        id_.validate()
        if Db.exec(Db.SQL_ID_EXISTS, (id_.value,))[0][0] == 0:
            raise NotFoundError(f'ID {id_} does not exist')

    @staticmethod
    def active(id_: TemplateId):
        """Checks if a template ID is active."""
        id_.validate()
        if Db.exec(Db.SQL_ID_ACTIVE, (id_.value,))[0][0] == 0:
            raise InvalidOperationError(f'ID {id_} not active')

    @staticmethod
    def archived(id_: TemplateId):
        """Checks if a template ID is archived."""
        id_.validate()
        if Db.exec(Db.SQL_ID_ARCHIVED, (id_.value,))[0][0] == 0:
            raise InvalidOperationError(f'ID {id_} not active')

    @staticmethod
    def unique(entity: Template):
        """Checks if a template ID is unique."""
        entity.id_.validate()
        entity.name.validate()
        entity.version.validate()
        res = Db.exec(Db.SQL_ID_FIND, (entity.name.value, entity.version.value))
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

    @staticmethod
    def list_active() -> List[TemplateSummary]:
        """Returns the list of active templates."""
        Db.init()
        res = Db.exec(Db.SQL_LIST_ACTIVE, None)
        return [Parse.summary(x) for x in res]

    @staticmethod
    def list_archived() -> List[TemplateSummary]:
        """Returns the list of archived templates."""
        res = Db.exec(Db.SQL_LIST_ARCHIVED, None)
        return [Parse.summary(x) for x in res]

    @staticmethod
    def load(id_: TemplateId) -> Template:
        """Loads an existing template."""
        Db.init()
        Validate.exists(id_)
        return Parse.detail(Db.exec(Db.SQL_LOAD, id_.serialize())[0])

    @staticmethod
    def render(id_: TemplateId, subs: Dict) -> str:
        """Renders an existing template."""
        Db.init()
        entity = Rule.load(id_)
        return Environment().from_string(entity.content.value).render(subs)

    @staticmethod
    def create(entity: Template):
        """Creates a new template."""
        Db.init()
        entity.validate()
        Validate.unique(entity)
        Db.exec(
            Db.SQL_CREATE,
            (entity.name.value, entity.version.value, entity.content.value))

    @staticmethod
    def update(entity: Template):
        """Updates an existing template."""
        Db.init()
        entity.validate()
        Validate.unique(entity)
        Db.exec(Db.SQL_UPDATE, entity.serialize())

    @staticmethod
    def archive(id_: TemplateId):
        """Archives an active template."""
        Db.init()
        Validate.exists(id_)
        Validate.active(id_)
        Db.exec(Db.SQL_ARCHIVE, id_.serialize())

    @staticmethod
    def restore(id_: TemplateId):
        """Restores an archived template."""
        Db.init()
        Validate.exists(id_)
        Validate.archived(id_)
        Db.exec(Db.SQL_RESTORE, id_.serialize())

    @staticmethod
    def delete(id_: TemplateId):
        """Deletes an archived template."""
        Db.init()
        Validate.exists(id_)
        Validate.archived(id_)
        Db.exec(Db.SQL_DELETE, id_.serialize())
