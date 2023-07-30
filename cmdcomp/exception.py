from typing import Never


class ConfigFileExtensionError(Exception):
    def __init__(self, extension: str) -> None:
        self._extension = extension

    def __str__(self) -> str:
        return f'config file extension "{self._extension}" is not supported.'


class NeverReach(Exception):
    def __init__(self, value: Never) -> None:
        self._value = value

    def __str__(self) -> str:
        return f"never reach: {self._value}"
