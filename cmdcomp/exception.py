class CmdcompError(Exception):
    pass


class FileExtensionError(CmdcompError):
    def __init__(self, file: str, extension: str) -> None:
        self._file = file
        self._extension = extension

    def __str__(self) -> str:
        return f'file extension "{self._extension}" of "{self._file}" is not supported.'
