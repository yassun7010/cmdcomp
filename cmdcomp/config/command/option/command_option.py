from typing import Annotated, Literal

from pydantic import BaseModel, Field


class CommandOption(BaseModel):
    type: Literal["command"]

    execute: Annotated[
        str,
        Field(title="command to execute."),
    ]
