from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V2ValuesArgument(Model):
    type: Literal["values"] | None = None

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    candidates: Annotated[
        str | list[str],
        Field(title="values of the argument."),
    ]
