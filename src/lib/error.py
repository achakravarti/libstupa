import enum


class ErrorCode(enum.Enum):
    NONE = 0
    DATABASE = 1
    NOTFOUND = 2
    MISSINGFLAG =3
    INVALIDOP = 4


class Error:
    """Represents a processing error. """

    def __init__(self, code, rule, msg):
        """Initialises this error. """
        self._code = code
        self._rule = rule
        self._msg = msg

    @property
    def code(self):
        """Gets the error code."""
        return self._code

    @code.setter
    def code(self, value):
        """Sets the error code."""
        self._code = value

    @property
    def rule(self):
        """Gets the rule where the error occurred."""
        return self._rule

    @rule.setter
    def rule(self, value):
        """Sets the rule where the error occurred."""
        self._rule = value

    @property
    def msg(self):
        """Gets the error message."""
        return self._msg

    @msg.setter
    def msg(self, value):
        """Sets the error message."""
        self._msg = value
