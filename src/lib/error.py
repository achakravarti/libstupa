import enum
import json
from dataclasses import asdict, dataclass


class Status(enum.Enum):
    """Represents an operation status.

    NONE: No error
    EDATABASE: A database error
    ENA: Item not found
    EOP: Invalid operation
    EPROP: Invalid data
    """
    NONE = 0
    EDATABASE = 1
    ENA = 2
    EOP = 3
    EPROP = 4


@dataclass
class Error:
    """Represents a processing error.

    code: Error code
    rule: Name of rule where error occurs
    msg: Error message
    """
    code: Status
    rule: str
    msg: str

    def json(self):
        """Gets the JSON representation of this error."""
        return json.dumps(asdict(self), indent=2)


@dataclass
class Template:
    """Represents a single template.

    id: Template ID
    name: Template name
    version: Template version
    content: Template content
    archived: Is template archived?
    """
    id: int
    name: str
    version: str
    content: str
    archived: bool

    def json(self):
        """Gets the JSON representation of this template."""
        return json.dumps(asdict(self), indent=2)


@dataclass
class TemplateSummary:
    """Represents a single template summary.

    id: Template ID
    name: Template name
    version: Template version
    """
    id: int
    name: str
    version: str

    def json(self):
        """Gets the JSON representation of this template."""
        return json.dumps(asdict(self), indent=2)
