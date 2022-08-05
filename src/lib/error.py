import enum
import json


class ErrorCode(enum.Enum):
    NONE = 0
    DATABASE = 1
    NOTFOUND = 2
    MISSINGFLAG =3
    INVALIDOP = 4


class Error:
    """Represents a processing error. """

    def __init__(self, code: ErrorCode, rule: str, msg: str):
        """Initialises this error. """
        self._code = code
        self._rule = rule
        self._msg = msg

    @property
    def code(self) -> ErrorCode:
        """Gets the error code."""
        return self._code

    @code.setter
    def code(self, value: ErrorCode):
        """Sets the error code."""
        self._code = value

    @property
    def rule(self) -> str:
        """Gets the rule where the error occurred."""
        return self._rule

    @rule.setter
    def rule(self, value: str):
        """Sets the rule where the error occurred."""
        self._rule = value

    @property
    def msg(self) -> str:
        """Gets the error message."""
        return self._msg

    @msg.setter
    def msg(self, value: str):
        """Sets the error message."""
        self._msg = value


    def __str__(self) -> str:
        """Gets the string representation of this error."""
        return 'Code: {}\nRule: {}\nMessage: {}'.format(
            self.code, self.rule, self.msg)


    def json(self) -> str:
        """Gets the JSON representation of this error."""
        jd = {
            'code': self.code,
            'rule': self.rule,
            'msg': self.msg
        }
        return json.dumps(jd, indent=2)
