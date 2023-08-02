from functools import reduce
from pathlib import Path

from mergedeep import merge

from cmdcomp import __version__
from cmdcomp.shell import ShellType
from cmdcomp.v1.command import (
    V1Candidates,
    V1Command,
    V1Completions,
    V1SubCommandsCommand,
    get_candidates,
    get_targets,
)
from cmdcomp.v1.config import V1Config


def generate_v1(shell: ShellType, config: V1Config):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
    )
    template = env.get_template(f"{shell.value}.sh.jinja")

    return template.render(
        app_name=config.app.name,
        app_aliases=config.app.aliases + config.root.aliases,
        completions_list=_generate_completions_list(config),
        version=__version__,
    )


def _generate_completions_list(config: V1Config):
    completions_list = [get_candidates(config.root)]

    _update_completions_list(
        completions_list,  # type: ignore
        config.root,
    )

    return completions_list


def _update_completions_list(
    completions_list: list[V1Completions],
    command: V1Command,
    keys: list[str] | None = None,
):
    if keys is None:
        keys = []

    if not isinstance(command, V1SubCommandsCommand):
        return

    for name, optional_subcommand in command.subcommands.items():
        subcommand = optional_subcommand or V1SubCommandsCommand.model_validate({})

        new_keys = keys + ["|".join(get_targets(name, subcommand))]

        _update_completions_list(completions_list, subcommand, new_keys)

        candidates: V1Candidates = get_candidates(subcommand)

        if len(candidates) == 0:
            continue

        while len(completions_list) < len(new_keys) + 1:
            completions_list.append({})

        merge(
            completions_list[len(new_keys)],  # type: ignore
            reduce(
                _swap_key_value,  # type: ignore
                reversed(new_keys),
                candidates,  # type: ignore
            ),
        )


def _swap_key_value(prev: V1Completions, key: str) -> V1Completions:
    return {key: prev}
