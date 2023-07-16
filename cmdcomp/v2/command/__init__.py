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
Keyword: TypeAlias = str
SubcommandName: TypeAlias = str


class V2Command(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    arguments__: Annotated[
        OrderedDict[
            Position | Keyword,
            str
            | list[str | V2ValueArgument]
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
    def arguments(self) -> OrderedDict[Position | Keyword, V2Argument]:
        return OrderedDict(
            [(k, _convert_argument(v)) for k, v in self.arguments__.items()]
        )


def _convert_argument(
    value: str
    | list[str | V2ValueArgument]
    | V2FileArgument
    | V2CommandArgument
    | V2FlagArgument
    | None,
) -> V2Argument:
    match value:
        case str():
            return V2ValuesArgument(type="values", values__=[value])

        case list():
            return V2ValuesArgument(
                type="values",
                values__=[
                    V2ValueArgument(value=v) if isinstance(v, str) else v for v in value
                ],
            )

        case None:
            return V2FlagArgument(type="flag")

        case _:
            return value
