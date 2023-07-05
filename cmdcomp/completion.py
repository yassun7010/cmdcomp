from functools import reduce
from pathlib import Path

from mergedeep import merge

from cmdcomp.config.command.subcommand import (
    Completions,
    Subcommands,
    get_candidates,
    get_targets,
)
from cmdcomp.config.config import Config
from cmdcomp.shell_type import ShellType


def generate(shell: ShellType, config: Config):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
    )
    template = env.get_template(f"{shell.value}.sh.jinja")

    return template.render(parse_config(config))


def parse_config(config: Config):
    completions_list: list[Completions] = [
        get_candidates(config.root.subcommands, config.root.options)
    ]

    update_completions_list(completions_list, config.root.subcommands)

    return {
        "appname": config.app.name,
        "app_aliases": config.app.aliases,
        "completions_list": completions_list,
    }


def update_completions_list(
    completions_list: list[Completions],
    subcommands: Subcommands,
    keys: list[str] | None = None,
) -> None:
    if keys is None:
        keys = []

    for name, subcommand in subcommands.items():
        new_keys = keys + ["|".join(get_targets(name, subcommand))]

        update_completions_list(completions_list, subcommand.subcommands, new_keys)

        candidates: Completions = subcommand.candidates

        if len(candidates) == 0:
            continue

        while len(completions_list) < len(new_keys) + 1:
            completions_list.append({})

        merge(
            completions_list[len(new_keys)],
            reduce(
                _swap_key_value,
                reversed(new_keys),
                candidates,
            ),
        )


def _swap_key_value(prev: Completions, key: str) -> Completions:
    return {key: prev}
