from functools import reduce
from operator import add
from typing import Annotated, NewType, OrderedDict

from pydantic import ConfigDict, Field

from cmdcomp.config.command.option import (
    OptionType,
    SpecificOptions,
    StrOption,
    StrOptions,
)
from cmdcomp.config.command.option.command_option import CommandOption
from cmdcomp.config.command.option.file_option import FileOption
from cmdcomp.config.model import Model
from cmdcomp.exception import NeverReach

SubcommandName = NewType("SubcommandName", str)

Candidate = SubcommandName | StrOption
Candidates = list[Candidate] | list[dict[OptionType, str]]

Completions = Candidates | dict[str, "Completions"]  # type: ignore


class SubCommandsCommand(Model):
    """A command that can specify a subcommand."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    options: Annotated[
        StrOptions,
        Field(
            title="options of the command.",
            default_factory=list,
        ),
    ]

    subcommands: OrderedDict[SubcommandName, "Command | None"] = Field(
        title="subcommands of the command.",
        default_factory=OrderedDict,
    )

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias


class SpecificOptionsCommand(Model):
    """A command that can specify options."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    options: Annotated[
        SpecificOptions,
        Field(
            title="options of the command.",
        ),
    ]

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias


Command = SubCommandsCommand | SpecificOptionsCommand

Subcommands = OrderedDict[SubcommandName, Command | None]


def get_targets(name: SubcommandName, subcommand: Command) -> list[str]:
    return [name] + subcommand.aliases


def get_candidates(command: Command) -> Candidates:
    match command:
        case SubCommandsCommand():
            return (
                [command.options]
                if isinstance(command.options, str)
                else command.options
            ) + reduce(
                add,
                [
                    get_targets(
                        name,
                        subcommand or SubCommandsCommand.model_validate({}),
                    )
                    for name, subcommand in command.subcommands.items()
                ],
                [],
            )
        case SpecificOptionsCommand():
            if isinstance(command.options, CommandOption):
                return [{"command": f"$({command.options.execute})"}]

            elif isinstance(command.options, FileOption):
                return [{"file": command.options.base_path}]
            else:
                raise NeverReach(command.options)
        case _:
            raise NeverReach(command)
