from typing import Annotated, OrderedDict

from pydantic import ConfigDict, Field

from cmdcomp.model import Model

from .argument import V2Argument


class V2Command(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    arguments: Annotated[
        OrderedDict[str | int, V2Argument | None],
        Field(title="arguments of the command."),
    ]
