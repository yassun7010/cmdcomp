from typing import Annotated, OrderedDict

from pydantic import ConfigDict, Field

from cmdcomp.model import Model
from cmdcomp.v2.command.argument.normal_argument import V2NormalArgument

from .argument import V2Argument


class V2Command(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    arguments__: Annotated[
        OrderedDict[str | int, str | list[str] | V2Argument],
        Field(title="arguments of the command.", alias="arguments"),
    ]

    @property
    def arguments(self) -> OrderedDict[str | int, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments__.items()
                if isinstance(v, V2Argument)
            ]
        )


def _convert_argument(value: str | list[str] | V2Argument) -> V2Argument:
    if isinstance(value, str):
        return V2NormalArgument(candidates=[value])
    elif isinstance(value, list):
        return V2NormalArgument(candidates=value)
    else:
        return value
