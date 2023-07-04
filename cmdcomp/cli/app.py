from logging import getLogger

from cmdcomp import __version__

logger = getLogger(__name__)


class App:
    @classmethod
    def run(
        cls,
        args: list[str] | None = None,
        *,
        throw_exception: bool = True,
    ) -> None:
        from argparse import ArgumentParser

        parser = ArgumentParser(
            prog="cmdcomp",
            description="A command-line tool for comparing commands.",
        )

        parser.add_argument(
            "--version", action="version", version=f"%(prog)s {__version__}"
        )

        space = parser.parse_args(args)

        try:
            print("Hello, World")

        except Exception as e:
            import colorama

            colorama.init()
            message = colorama.Back.RED + " Error " + colorama.Back.RESET + f": {e}"

            if space.verbose:
                logger.exception(message)
            else:
                logger.error(message)

            if throw_exception:
                raise e
