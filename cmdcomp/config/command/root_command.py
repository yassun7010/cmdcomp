from typing import Annotated, OrderedDict

from pydantic import BaseModel, Field

from cmdcomp.config.command.option import Options
from cmdcomp.config.command.subcommand import Subcommand, SubcommandName


class RootCommand(BaseModel):
    """
    Root command of the cli app.
    """

    options: Annotated[
        Options,
        Field(
            title="options of the command.",
            default_factory=list,
        ),
    ]

    subcommands: Annotated[
        OrderedDict[SubcommandName, Subcommand],
        Field(
            title="subcommands of the cli command.",
            default_factory=OrderedDict,
        ),
    ]
