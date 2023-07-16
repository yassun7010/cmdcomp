from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V1FileOption(Model):
    """a: complete with a relative path from the directory specified by base_path."""

    type: Literal["file"]

    base_path: Annotated[
        str,
        Field(title="path of the directory from which to base filename completion."),
    ]
