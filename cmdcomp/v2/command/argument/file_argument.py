from typing import Literal

from pydantic import Field

from cmdcomp.model import Model


class V2FileArgument(Model):
    type: Literal["file"]

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )

    base_path: str | None = Field(
        title="path of the directory from which to base filename completion.",
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
