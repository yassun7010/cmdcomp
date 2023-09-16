from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model
from cmdcomp.v2.mixin.has_alias import HasAlias


class V2FileArgument(HasAlias, Model):
    """completion of file names starting from the specified directory."""

    type: Literal["file"]

    description: Annotated[
        str | None,
        Field(title="description of the argument."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the argument."),
    ] = None

    base_path: Annotated[
        str | None,
        Field(title="path of the directory from which to base filename completion."),
    ] = None
