from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V2CommandArgument(Model):
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

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        elif isinstance(self.alias, list):
            return self.alias
        else:
            return []
