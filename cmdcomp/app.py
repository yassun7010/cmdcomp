class App:
    @classmethod
    def run(cls, args: list[str] | None = None) -> None:
        import logging
        from argparse import ArgumentParser, BooleanOptionalAction, FileType
        from logging import getLogger

        import argcomplete
        from rich.console import Console
        from rich.logging import RichHandler

        from cmdcomp import __version__
        from cmdcomp.completion import generate
        from cmdcomp.config import load
        from cmdcomp.shell import ShellType

        parser = ArgumentParser(
            prog="cmdcomp",
            description="A command-line tool for comparing commands.",
        )

        parser.add_argument(
            "--version",
            action="version",
            version=f"%(prog)s {__version__}",
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

        parser.add_argument(
            "--verbose",
            action=BooleanOptionalAction,
            help="output verbose log.",
        )

        argcomplete.autocomplete(parser)

        space = parser.parse_args(args)

        logging.basicConfig(
            format="%(message)s",
            handlers=[
                RichHandler(
                    level=logging.DEBUG if space.verbose else logging.INFO,
                    console=Console(stderr=True),
                    show_time=False,
                    show_path=False,
                    rich_tracebacks=True,
                )
            ],
        )
        logger = getLogger(__name__)

        try:
            print(
                generate(space.shell_type, load(space.file)),
                file=space.output_file,
            )

        except Exception as e:
            if space.verbose:
                logger.exception(e)
            else:
                logger.error(e)

            raise e
