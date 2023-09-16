from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2CommandArgument(HasAlias, Model):
    """complete with the result of executing the command."""

    type: Annotated[
        Literal["command"],
        Field(title="complete with the result of executing the command."),
    ]

    description: Annotated[
        str | None,
        Field(title="description of the argument."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the argument."),
    ] = None

    execute: Annotated[
        str,
        Field(title="command to execute."),
    ]
