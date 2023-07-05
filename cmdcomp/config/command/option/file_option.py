from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.config.model import Model


class FileOption(Model):
    type: Literal["file"]

    base_path: Annotated[
        str,
        Field(title="path of the directory from which to base filename completion."),
    ]
