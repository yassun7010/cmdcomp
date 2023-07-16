from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.v1.v1_config.model import Model


class CommandOption(Model):
    """complete with the result of executing the command in the Shell command."""

    type: Literal["command"]

    execute: Annotated[
        str,
        Field(title="command to execute."),
    ]
