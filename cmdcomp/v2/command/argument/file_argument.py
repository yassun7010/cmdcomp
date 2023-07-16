from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V2FileArgument(Model):
    type: Literal["file"]

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    base_path: Annotated[
        str,
        Field(title="path of the directory from which to base filename completion."),
    ]
