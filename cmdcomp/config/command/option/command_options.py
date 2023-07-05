from typing import Annotated, Literal

from pydantic import BaseModel, Field


class CommandOptions(BaseModel):
    type: Literal["command"]

    execute: Annotated[
        str,
        Field(title="command to execute."),
    ]
