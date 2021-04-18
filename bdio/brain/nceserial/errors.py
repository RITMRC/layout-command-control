class NceError(Exception):
    """Base class for NCE exceptions in this module"""

    pass


class UnsupportedCommandError(NceError):
    def __init__(self, command):
        self.command = command