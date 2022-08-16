import json
from dataclasses import asdict, dataclass
from typing import Tuple, List
from .error import InvalidPropertyError


@dataclass
class TemplateId:
    """Template ID value object."""
    value: int

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if self.value is None or self.value < 0:
            raise InvalidPropertyError(
                'template ID must be positive integer')


@dataclass
class TemplateName:
    """Template name value object."""
    value: str

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if not self.value:
            raise InvalidPropertyError('template name required')


@dataclass
class TemplateVersion:
    """Template version value object."""
    value: str

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if not self.value:
            raise InvalidPropertyError('template version required')


@dataclass
class TemplateContent:
    """Template content value object."""
    value: str

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if not self.value:
            raise InvalidPropertyError('template content required')


@dataclass
class Template:
    """Represents a single template.

    id_: Template ID
    name: Template name
    version: Template version
    content: Template content
    archived: Is template archived?
    """
    id_: TemplateId
    name: TemplateName
    version: TemplateVersion
    content: TemplateContent
    archived: bool

    def validate(self):
        """Checks whether this entity is valid."""
        self.id_.validate()
        self.name.validate()
        self.version.validate()
        self.content.validate()

    def serialize(self) -> Tuple:
        """Serializes this entity to a tuple."""
        return (
            self.id_.value,
            self.name.value,
            self.version.value,
            self.content.value)

    def json(self):
        """Gets the JSON representation of this template."""
        j = '{{"id":{},"name":"{}","version":"{}", "content":"{}","archived":{}}}'.format(
            self.id_, self.name, self.version, self.content, self.archived)
        return json.loads(j)


@dataclass
class TemplateSummary:
    """Represents a single template summary.

    id_: Template ID
    name: Template name
    version: Template version
    """
    id_: TemplateId
    name: TemplateName
    version: TemplateVersion

    def validate(self):
        """Checks whether this entity is valid."""
        self.id_.validate()
        self.name.validate()
        self.version.validate()

    def json(self):
        """Gets the JSON representation of this template."""
        j = '{{"id":{},"name":"{}","version":"{}"}}'.format(
            self.id_, self.name, self.version)
        return json.loads(j)

    @staticmethod
    def json_list(lst: List):
        """Gets the JSON representation of a list of temmplate summaries."""
        j = '['
        for x in lst[:-1]:
            j = j + json.dumps(x.json()) + ','
        j = j + json.dumps(lst[-1].json()) + ']'
        return json.loads(j)
