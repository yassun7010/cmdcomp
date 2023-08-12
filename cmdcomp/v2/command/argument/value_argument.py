from typing import Annotated

from pydantic import Field

from cmdcomp.model import Model


class V2ValueArgument(Model):
    value: Annotated[
        str,
        Field(title="value of the argument."),
    ]
