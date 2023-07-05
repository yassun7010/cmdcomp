from argparse import BooleanOptionalAction, FileType
from logging import getLogger

from cmdcomp import __version__
from cmdcomp.cli.subcommand.completion import generate
from cmdcomp.config.config import load
from cmdcomp.generator.shell_type import ShellType

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

        parser.add_argument(
            "--file",
            "-f",
            required=True,
            metavar="FILE",
            type=FileType("rb"),
            help="completion config file.",
        )

        parser.add_argument(
            "--shell-type",
            required=True,
            metavar="SHELL_TYPE",
            type=ShellType,
            choices=list(ShellType),
            help="target shell type.",
        )

        parser.add_argument(
            "--output-file",
            "-o",
            metavar="OUTPUT_FILE",
            type=FileType("w"),
            help="output file (Default='stdout').",
        )

        parser.add_argument(
            "--verbose",
            "-v",
            action=BooleanOptionalAction,
            help="output verbose log.",
        )

        space = parser.parse_args(args)

        try:
            print(
                generate(space.shell_type, load(space.file)),
                file=space.output_file,
            )

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
