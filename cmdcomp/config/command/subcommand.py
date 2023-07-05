from typing import Annotated, NewType, OrderedDict

from pydantic import BaseModel, ConfigDict, Field

from cmdcomp.config.command.option import Options

SubcommandName = NewType("SubcommandName", str)


class Subcommand(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    options: Annotated[
        Options,
        Field(
            title="options of the command.",
            default_factory=list,
        ),
    ]

    subcommands: OrderedDict[SubcommandName, "Subcommand"] = Field(
        title="subcommands of the command.",
        default_factory=OrderedDict,
    )


Subcommands = OrderedDict[SubcommandName, Subcommand]
