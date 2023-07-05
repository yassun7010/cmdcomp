from typing import Annotated

from pydantic import BaseModel, Field


class AppInfo(BaseModel):
    name: Annotated[str, Field(title="your cli app name.")]
    alias: str | list[str] = Field(
        title="alias of the cli command name.",
        default_factory=list,
    )

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias
