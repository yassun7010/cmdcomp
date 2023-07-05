from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.config.model import Model


class CommandOption(Model):
    type: Literal["command"]

    execute: Annotated[
        str,
        Field(title="command to execute."),
    ]
