from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2FlagArgument(HasAlias, Model):
    """completion of flags to support enable/disable."""

    type: Annotated[
        Literal["flag"],
        Field(title="completion of flags to support enable/disable."),
    ]

    description: Annotated[
        str | None,
        Field(title="description of the argument."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the argument."),
    ] = None
