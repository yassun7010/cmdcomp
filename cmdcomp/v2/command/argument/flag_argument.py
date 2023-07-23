from typing import Literal

from pydantic import Field

from cmdcomp.model import Model


class V2FlagArgument(Model):
    type: Literal["flag"]

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        elif isinstance(self.alias, list):
            return self.alias
        else:
            return []
