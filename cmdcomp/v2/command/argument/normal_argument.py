from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V2NormalArgument(Model):
    type: Literal["normal"] | None = None

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    candidates: Annotated[
        str | list[str],
        Field(title="candidates of the argument."),
    ]
