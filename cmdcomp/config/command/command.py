from typing import Annotated

from pydantic import BaseModel, Field

from cmdcomp.config.alias import Alias
from cmdcomp.config.command.options import Options


class Command(BaseModel):
    alias: Annotated[
        Alias,
        Field(title="alias of the command."),
    ]

    options: Annotated[
        Options,
        Field(title="options of the command."),
    ]
