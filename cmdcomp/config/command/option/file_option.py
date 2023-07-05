from typing import Annotated, Literal

from pydantic import BaseModel, Field


class FileOption(BaseModel):
    type: Literal["file"]

    base_path: Annotated[
        str,
        Field(title="path of the directory from which to base filename completion."),
    ]
