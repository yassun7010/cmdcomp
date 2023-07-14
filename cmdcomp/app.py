class App:
    @classmethod
    def run(
        cls,
        args: list[str] | None = None,
        *,
        throw_exception: bool = True,
    ) -> None:
        import logging
        from argparse import ArgumentParser, BooleanOptionalAction, FileType
        from logging import getLogger

        from rich.logging import RichHandler

        from cmdcomp import __version__
        from cmdcomp.completion import generate
        from cmdcomp.config.config import load
        from cmdcomp.shell_type import ShellType

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
            help="config file ('.json', '.yaml', '.toml' support).",
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
            help="output file (Default=stdout).",
        )

        parser.add_argument(
            "--verbose",
            "-v",
            action=BooleanOptionalAction,
            help="output verbose log.",
        )

        logging.basicConfig(
            format="%(message)s",
            handlers=[
                RichHandler(
                    show_time=False,
                    show_path=False,
                    rich_tracebacks=True,
                )
            ],
        )
        logger = getLogger(__name__)

        space = parser.parse_args(args)

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
