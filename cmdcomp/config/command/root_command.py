from typing import Annotated, OrderedDict

from pydantic import BaseModel, Field

from cmdcomp.config.command.subcommand import Subcommand, SubcommandName


class RootCommand(BaseModel):
    """
    Root command of the cli app.
    """

    alias: Annotated[
        str | list[str] | None,
        Field(
            title="alias of the cli command.",
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
