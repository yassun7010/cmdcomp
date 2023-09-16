from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2RelayArgument(HasAlias, Model):
    """relay completion of other command."""

    type: Annotated[
        Literal["relay"],
        Field(title="relay completion of other command."),
    ]

    description: Annotated[
        str | None,
        Field(title="description of the argument."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the argument."),
    ] = None

    target: Annotated[str, Field(title="relay target.")]
