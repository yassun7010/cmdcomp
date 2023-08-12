from typing import Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2FileArgument(HasAlias, Model):
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
