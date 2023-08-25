from typing import Annotated

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2AppInfo(HasAlias, Model):
    """your cli app info."""

    name: Annotated[
        str,
        Field(title="your cli app name."),
    ]

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the cli app name."),
    ] = None
