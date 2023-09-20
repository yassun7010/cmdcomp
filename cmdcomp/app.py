import argparse
import logging
import sys
from argparse import BooleanOptionalAction, FileType
from pathlib import Path
from typing import NoReturn

from rich.console import Console as RichConsole
from rich.logging import RichHandler
from rich_argparse import RichHelpFormatter

from cmdcomp import __version__
from cmdcomp.shell import ShellType


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> NoReturn:
        self.print_usage(sys.stderr)
        raise ValueError(message)


class App:
    @classmethod
    def run(cls, args: list[str] | None = None) -> None:
        RichHelpFormatter.styles["lit"] = RichHelpFormatter.styles["argparse.metavar"]

        parser = ArgumentParser(
            prog="cmdcomp",
            description="shell completion file generator.",
            formatter_class=RichHelpFormatter,
        )

        parser.add_argument(
            "--version",
            action="version",
            version=f"[argparse.prog]%(prog)s[/] {__version__}",
        )

        parser.add_argument(
            "--verbose",
            action=BooleanOptionalAction,
            help="output verbose log.",
        )

        parser.add_argument(
            "--file",
            "--config",
            "-f",
            required=True,
            type=FileType("rb"),
            help="config file path. supported formats are "
            + '[lit]".json"[/], [lit]".yaml"[/], [lit]".toml"[/] and [lit]".jinja"[/].',
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
            type=Path,
            help="output file path. default is [lit]stdout[/].",
        )

        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            handlers=[
                RichHandler(
                    level=logging.DEBUG,
                    console=RichConsole(stderr=True),
                    show_time=False,
                    show_path=False,
                    rich_tracebacks=True,
                )
            ],
        )
        logger = logging.getLogger(__name__)

        try:
            space = parser.parse_args(args)
        except Exception as e:
            logger.error(e)

            raise e

        logging.root.setLevel(logging.DEBUG if space.verbose else logging.INFO)

        try:
            from cmdcomp import completion, config

            output_file: Path | None = space.output_file

            output = completion.generate(
                space.shell_type,
                config.load(space.file),
            )

            if output_file:
                with open(output_file, "w") as f:
                    f.write(output)
            else:
                print(output)

        except Exception as e:
            if space.verbose:
                logger.exception(e)
            else:
                logger.error(e)

            raise e
