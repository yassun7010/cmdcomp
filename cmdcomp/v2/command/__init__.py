from typing import Annotated, OrderedDict, TypeAlias

from pydantic import ConfigDict, Field

from cmdcomp.model import Model
from cmdcomp.v2.command.argument.command_argument import V2CommandArgument
from cmdcomp.v2.command.argument.file_argument import V2FileArgument
from cmdcomp.v2.command.argument.flag_argument import V2FlagArgument
from cmdcomp.v2.command.argument.values_argument import (
    V2ValueArgument,
    V2ValuesArgument,
)

from .argument import V2Argument

Position: TypeAlias = int
Keyword = Annotated[str, Field(pattern=r"^--?[a-zA-Z0-9_-]+$")]
SubcommandName: TypeAlias = str


class V2PoristionalArgumentsCommand(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    arguments: Annotated[
        OrderedDict[
            Position | Keyword,
            str
            | list[str]
            | V2ValuesArgument
            | V2FileArgument
            | V2CommandArgument
            | V2FlagArgument
            | None,
        ],
        Field(
            title="arguments of the command.",
            alias="arguments",
        ),
    ]

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias

    @property
    def subcommands(self) -> OrderedDict[SubcommandName, "V2Command"]:
        return OrderedDict()

    @property
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, int)
            ]
        )

    @property
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, str)
            ]
        )


class V2SubcommandsCommand(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    arguments: Annotated[
        OrderedDict[
            Keyword,
            str
            | list[str]
            | V2ValuesArgument
            | V2FileArgument
            | V2CommandArgument
            | V2FlagArgument
            | None,
        ],
        Field(
            title="arguments of the command.",
            alias="arguments",
        ),
    ]

    subcommands: OrderedDict[SubcommandName, "V2Command"] = Field(
        title="subcommands of the command.",
        default_factory=OrderedDict,
    )

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias

    @property
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict()

    @property
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, str)
            ]
        )


def _convert_argument(
    value: str
    | list[str]
    | V2ValuesArgument
    | V2FileArgument
    | V2CommandArgument
    | V2FlagArgument
    | None,
) -> V2Argument:
    match value:
        case str():
            return V2ValuesArgument(type="values", items=[value])

        case list():
            return V2ValuesArgument(
                type="values",
                items=[V2ValueArgument(value=v) for v in value],
            )

        case None:
            return V2FlagArgument(type="flag")

        case _:
            return value


V2Command = V2PoristionalArgumentsCommand | V2SubcommandsCommand
