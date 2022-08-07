import json
from dataclasses import asdict, dataclass
from typing import Tuple
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
                'Template ID must be an integer greater than 0')


@dataclass
class TemplateName:
    """Template name value object."""
    value: str

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if self.value is not None and self.value != '':
            raise InvalidPropertyError('Template name must be an specified')


@dataclass
class TemplateVersion:
    """Template version value object."""
    value: str

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if self.value is not None and self.value != '':
            raise InvalidPropertyError('Template version must be an specified')


@dataclass
class TemplateContent:
    """Template content value object."""
    value: str

    def serialize(self) -> Tuple:
        """Serializes this value object to a tuple."""
        return (self.value,)

    def validate(self):
        """Checks if the value is valid."""
        if self.value is not None and self.value != '':
            raise InvalidPropertyError('Template content must be an specified')


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
        return json.dumps(asdict(self), indent=2)


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
        return json.dumps(asdict(self), indent=2)
