from collections import OrderedDict
from functools import cached_property
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
    type: Literal["values"]  # NOTE: Perhaps it should have been "select."

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )

    raw_values: Annotated[
        str | list[str | V2ValueArgument] | OrderedDict[str, str | V2ValueArgument],
        Field(
            title="values of the argument.",
            alias="values",
        ),
    ]

    @cached_property
    def values(self) -> list[V2ValueArgument]:
        match self.raw_values:
            case str():
                return [V2ValueArgument(value=self.raw_values)]

            case list():
                return [
                    v if isinstance(v, V2ValueArgument) else V2ValueArgument(value=v)
                    for v in self.raw_values
                ]

            case OrderedDict():
                return [
                    V2ValueArgument(value=v) if isinstance(v, str) else v
                    for v in self.raw_values.values()
                ]

            case _:
                raise NeverReach(self.raw_values)

    @cached_property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        elif isinstance(self.alias, list):
            return self.alias
        else:
            return []
