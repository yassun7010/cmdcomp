from functools import reduce
from operator import add
from typing import Annotated, NewType, OrderedDict

from pydantic import ConfigDict, Field

from cmdcomp.exception import NeverReach
from cmdcomp.model import Model
from cmdcomp.v1.command.option import V1OptionType, V1SpecificOptions, V1StrOption
from cmdcomp.v1.command.option.command_option import V1CommandOption
from cmdcomp.v1.command.option.file_option import V1FileOption

V1SubcommandName = NewType("V1SubcommandName", str)

V1Candidate = V1SubcommandName | V1StrOption
V1Candidates = list[V1Candidate] | list[dict[V1OptionType, str]]

V1Completions = V1Candidates | dict[str, "V1Completions"]  # type: ignore


class V1SubCommandsCommand(Model):
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
        V1StrOption | list[V1StrOption],
        Field(
            title="options of the command.",
            default_factory=list,
        ),
    ]

    subcommands: OrderedDict[V1SubcommandName, "V1Command | None"] = Field(
        title="subcommands of the command.",
        default_factory=OrderedDict,
    )

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias


class V1SpecificOptionsCommand(Model):
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
        V1SpecificOptions,
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


V1Command = V1SubCommandsCommand | V1SpecificOptionsCommand

Subcommands = OrderedDict[V1SubcommandName, V1Command | None]


def get_targets(name: V1SubcommandName, subcommand: V1Command) -> list[str]:
    return [name] + subcommand.aliases


def get_candidates(command: V1Command) -> V1Candidates:
    match command:
        case V1SubCommandsCommand():
            return (
                [command.options]
                if isinstance(command.options, str)
                else command.options
            ) + reduce(
                add,
                [
                    get_targets(
                        name,
                        subcommand or V1SubCommandsCommand.model_validate({}),
                    )
                    for name, subcommand in command.subcommands.items()
                ],
                [],
            )
        case V1SpecificOptionsCommand():
            if isinstance(command.options, V1CommandOption):
                return [{"command": f"$({command.options.execute})"}]

            elif isinstance(command.options, V1FileOption):
                return [{"file": command.options.base_path}]
            else:
                raise NeverReach(command.options)
        case _:
            raise NeverReach(command)
