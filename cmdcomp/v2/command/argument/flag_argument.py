from typing import Literal

from pydantic import Field

from cmdcomp.model import Model


class V2FlagArgument(Model):
    type: Literal["flag"] = "flag"
    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    alias: str | list[str] | None = Field(
        title="alias of the argument.",
        default=None,
    )
