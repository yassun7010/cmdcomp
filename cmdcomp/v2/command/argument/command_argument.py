from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2CommandArgument(HasAlias, Model):
    """complete with the result of executing the command in the Shell command."""

    type: Literal["command"]

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )

    execute: Annotated[
        str,
        Field(title="command to execute."),
    ]
