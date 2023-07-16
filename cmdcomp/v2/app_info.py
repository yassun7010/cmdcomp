from typing import Annotated

from pydantic import Field

from cmdcomp.model import Model


class V2AppInfo(Model):
    """your cli app info."""

    name: Annotated[str, Field(title="your cli app name.")]

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the cli app name.",
            default_factory=list,
        ),
    ]

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias
