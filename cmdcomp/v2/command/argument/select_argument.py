from collections import OrderedDict
from functools import cached_property
from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.exception import NeverReach
from cmdcomp.model import Model
from cmdcomp.v2.command.argument.value_argument import V2ValueArgument
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2SelectArgument(HasAlias, Model):
    type: Literal["select"]

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )

    raw_values: Annotated[
        list[str | V2ValueArgument] | OrderedDict[str, str | V2ValueArgument],
        Field(
            title="candidate selection.",
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
