"""Main exception class for raising server exceptions"""


class ServerError(Exception):
    """Base class for raising errors for a server exceptions"""

    pass


class KeyNotProvidedError(ServerError):
    """Raised when the key is not provided"""


class ResourceNotFound(ServerError):
    """Raised when the resource for a key is not found"""
