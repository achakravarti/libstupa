import enum
import json
from dataclasses import asdict, dataclass


class Status(enum.Enum):
    NONE = 0
    EDATABASE = 1
    ENOTFOUND = 2
    EFLAG =3
    EOP = 4
    EPROP = 5


@dataclass
class Error:
    """Represents a processing error. """
    code: Status
    rule: str
    msg: str

    def json(self):
        """Gets the JSON representation of this error."""
        return json.dumps(asdict(self), indent=2)


@dataclass
class Template:
    """Represents a single template"""
    id: int
    title: str
    version: str
    content: str
    archived: bool

    def json(self):
        """Gets the JSON representation of this template."""
        return json.dumps(asdict(self), indent=2)


@dataclass
class TemplateSummary:
    """Represents a single template summary"""
    id: int
    title: str
    version: str

    def json(self):
        """Gets the JSON representation of this template."""
        return json.dumps(asdict(self), indent=2)
