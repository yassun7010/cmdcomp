from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2SelectArgument(HasAlias, Model):
    """completion for choosing from options."""

    type: Annotated[
        Literal["select"],
        Field(title="completion for choosing from options."),
    ]

    description: Annotated[
        str | None,
        Field(title="description of the argument."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the argument."),
    ] = None

    raw_options: Annotated[
        list[str] | None,
        Field(
            title="completion candidates.",
            alias="options",
        ),
    ] = None

    values: Annotated[
        list[str] | str | None,
        Field(
            title="completion candidates.",
            description="this field is deprecated. use `options` instead.",
            json_schema_extra={"deprecated": True},
        ),
    ] = None

    @property
    def options(self) -> list[str]:
        if self.raw_options is not None:
            return self.raw_options
        if self.values is None:
            return []
        elif isinstance(self.values, str):
            return [self.values]
        else:
            return self.values
