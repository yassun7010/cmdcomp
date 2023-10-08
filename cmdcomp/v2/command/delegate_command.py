from typing import Annotated, Literal

from pydantic import Field

from .empty_command import V2EmptyCommand


class V2DelegateCommand(V2EmptyCommand):
    """delegate completion of other command."""

    type: Annotated[
        Literal["delegate"],
        Field(title="delegate completion of other command."),
    ]

    description: Annotated[
        str | None,
        Field(title="description of the argument."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the argument."),
    ] = None

    target: Annotated[str, Field(title="delegate target.")]
