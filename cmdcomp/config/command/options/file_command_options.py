from pathlib import Path
from typing import Annotated, Literal

from pydantic import BaseModel, Field


class FileCommandOptions(BaseModel):
    type: Literal["file"]

    base_path: Annotated[
        Path,
        Field(title="path of the directory from which to base filename completion."),
    ]
