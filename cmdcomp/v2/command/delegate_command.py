from functools import cached_property
from typing import Annotated, Literal, OrderedDict

from pydantic import Field
from typing_extensions import override

from cmdcomp.v2.command.argument import V2Argument
from cmdcomp.v2.command.base_command import InputArgument, Keyword, convert_argument

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

    target: Annotated[
        str | list[str],
        Field(
            title="delegate target command name.",
            examples=[
                "aws",
                ["aws", "s3"],
                ["aws", "s3", "ls"],
            ],
        ),
    ]

    arguments: OrderedDict[Keyword, InputArgument | None] = Field(
        title="arguments of the command.",
        description='argment key allow keyword string (like "--f", "-f") only.',
        default_factory=OrderedDict,
    )

    @property
    def targets(self) -> list[str]:
        if isinstance(self.target, str):
            return [self.target]
        else:
            return self.target

    @cached_property
    @override
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, str)
            ]
        )
