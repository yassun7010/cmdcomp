from functools import cached_property
from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
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
        str | list[str],
        Field(
            title="candidate selection.",
            alias="values",
        ),
    ]

    @cached_property
    def values(self) -> list[str]:
        match self.raw_values:
            case str():
                return [self.raw_values]

            case list():
                return self.raw_values
