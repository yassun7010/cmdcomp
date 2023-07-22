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

    values__: Annotated[
        str | list[str | V2ValueArgument] | OrderedDict[str, str | V2ValueArgument],
        Field(
            title="values of the argument.",
            serialization_alias="values",
        ),
    ]

    @property
    def values(self) -> list[V2ValueArgument]:
        match self.values__:
            case str():
                return [V2ValueArgument(value=self.values__)]

            case list():
                return [
                    v if isinstance(v, V2ValueArgument) else V2ValueArgument(value=v)
                    for v in self.values__
                ]

            case OrderedDict():
                return [
                    V2ValueArgument(value=v) if isinstance(v, str) else v
                    for v in self.values__.values()
                ]

            case _:
                raise NeverReach(self.values__)
