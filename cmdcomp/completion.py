from pathlib import Path
from typing import NewType

from cmdcomp.config.command.option.option import Option
from cmdcomp.config.command.option.option_type import OptionType
from cmdcomp.config.command.subcommand import Subcommand
from cmdcomp.config.config import Config
from cmdcomp.shell_type import ShellType

SubCommandName = NewType("SubCommandName", str)
Candidate = SubCommandName | Option
Candidates = list[Candidate] | list[dict[OptionType, str]]

Completions = Candidates | dict[str, "Completions"]  # type: ignore


def generate(shell: ShellType, config: Config):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
    )
    template = env.get_template(f"{shell.value}.sh.jinja")

    return template.render(parse_config(config))


def parse_config(config: Config):
    completions_list: list[Completions] = []

    return {
        "appname": config.app.name,
        "app_aliases": config.app.aliases,
        "completions_list": completions_list,
    }


def update_completions_list(
    completions_list: list[Completions],
    subcommand: Subcommand,
    keys: list[str] | None = None,
) -> None:
    if keys is None:
        keys = []
