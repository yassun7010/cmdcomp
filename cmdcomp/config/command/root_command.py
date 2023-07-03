from typing import Annotated, OrderedDict

from pydantic import BaseModel, Field

from cmdcomp.config.alias import Alias
from cmdcomp.config.command.command import Command
from cmdcomp.config.command.name import CommandName


class RootCommand(BaseModel):
    """
    Root command of the cli app.
    """

    alias: Annotated[Alias | None, Field(title="alias of the cli command.")]
    subcommands: Annotated[
        OrderedDict[CommandName, Command],
        Field(title="subcommands of the cli command."),
    ]
