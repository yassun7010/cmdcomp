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

    options: Annotated[
        list[str],
        Field(title="completion candidates."),
    ]
