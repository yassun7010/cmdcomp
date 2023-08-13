import logging
from argparse import ArgumentParser, BooleanOptionalAction, FileType

from rich.console import Console as RichConsole
from rich.logging import RichHandler

from cmdcomp import __version__, completion, config
from cmdcomp.shell import ShellType


class App:
    @classmethod
    def run(cls, args: list[str] | None = None) -> None:
        parser = ArgumentParser(
            prog="cmdcomp",
            description="ShellScript completion generator tool.",
        )

        parser.add_argument(
            "--version",
            action="version",
            version=f"%(prog)s {__version__}",
        )

        parser.add_argument(
            "--verbose",
            action=BooleanOptionalAction,
            help="output verbose log.",
        )

        parser.add_argument(
            "--file",
            "-f",
            required=True,
            type=FileType("rb"),
            help="config file ('.json', '.yaml', '.toml' support).",
        )

        parser.add_argument(
            "--shell-type",
            required=True,
            type=ShellType,
            choices=list(ShellType),
            help="target shell type.",
        )

        parser.add_argument(
            "--output-file",
            "-o",
            type=FileType("w"),
            help="output file (Default=stdout).",
        )

        space = parser.parse_args(args)

        level = logging.DEBUG if space.verbose else logging.INFO
        logging.basicConfig(
            format="%(message)s",
            level=level,
            handlers=[
                RichHandler(
                    level=level,
                    console=RichConsole(stderr=True),
                    show_time=False,
                    show_path=False,
                    rich_tracebacks=True,
                )
            ],
        )
        logger = logging.getLogger(__name__)

        try:
            print(
                completion.generate(
                    space.shell_type,
                    config.load(space.file),
                ),
                file=space.output_file,
            )

        except Exception as e:
            if space.verbose:
                logger.exception(e)
            else:
                logger.error(e)

            raise e
