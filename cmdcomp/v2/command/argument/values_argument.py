from collections import OrderedDict
from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.exception import NeverReach
from cmdcomp.model import Model


class V2ValueArgument(Model):
    value: Annotated[
        str,
        Field(title="value of the argument."),
    ]

    def __str__(self) -> str:
        return self.value


class V2ValuesArgument(Model):
    type: Literal["values"]

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )

    values: Annotated[
        str | list[str | V2ValueArgument] | OrderedDict[str, str | V2ValueArgument],
        Field(title="values of the argument."),
    ]

    @property
    def items(self) -> list[V2ValueArgument]:
        match self.values:
            case str():
                return [V2ValueArgument(value=self.values)]

            case list():
                return [
                    v if isinstance(v, V2ValueArgument) else V2ValueArgument(value=v)
                    for v in self.values
                ]

            case OrderedDict():
                return [
                    V2ValueArgument(value=v) if isinstance(v, str) else v
                    for v in self.values.values()
                ]

            case _:
                raise NeverReach(self.values)

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        elif isinstance(self.alias, list):
            return self.alias
        else:
            return []
