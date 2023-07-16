from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V2FileArgument(Model):
    type: Literal["file"]

    base_path: Annotated[
        str,
        Field(title="path of the directory from which to base filename completion."),
    ]
