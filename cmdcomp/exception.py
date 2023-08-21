from typing import Never


class FileExtensionError(Exception):
    def __init__(self, file: str, extension: str) -> None:
        self._file = file
        self._extension = extension

    def __str__(self) -> str:
        return f'file extension "{self._extension}" of "{self._file}" is not supported.'


class NeverReach(Exception):
    def __init__(self, value: Never) -> None:
        self._value = value

    def __str__(self) -> str:
        return f"never reach: {self._value}"
