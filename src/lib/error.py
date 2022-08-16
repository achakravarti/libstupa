
class DatabaseError(Exception):
    """Denotes a database exception."""
    pass


class NotFoundError(Exception):
    """Denotes a not found error."""
    pass


class InvalidOperationError(Exception):
    """Denotes an invalid operation exception."""
    pass


class InvalidPropertyError(Exception):
    """Denotes an invalid property exception."""
    pass
