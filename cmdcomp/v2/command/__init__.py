from typing import Annotated, OrderedDict

from pydantic import ConfigDict, Field

from cmdcomp.model import Model
from cmdcomp.v2.command.argument.command_argument import V2CommandArgument
from cmdcomp.v2.command.argument.file_argument import V2FileArgument
from cmdcomp.v2.command.argument.values_argument import (
    V2ValueArgument,
    V2ValuesArgument,
)

from .argument import V2Argument


class V2Command(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    arguments__: Annotated[
        OrderedDict[
            str | int,
            str | list[str | V2ValueArgument] | V2FileArgument | V2CommandArgument,
        ],
        Field(title="arguments of the command.", alias="arguments"),
    ]

    @property
    def arguments(self) -> OrderedDict[str | int, V2Argument]:
        return OrderedDict(
            [(k, _convert_argument(v)) for k, v in self.arguments__.items()]
        )


def _convert_argument(
    value: str | list[str | V2ValueArgument] | V2FileArgument | V2CommandArgument,
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

        case _:
            return value
