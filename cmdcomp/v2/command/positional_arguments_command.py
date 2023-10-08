from functools import cached_property
from typing import TYPE_CHECKING, Annotated, Literal, OrderedDict

from pydantic import Field
from typing_extensions import override

from cmdcomp.v2.command.base_command import (
    InputArgument,
    Keyword,
    Position,
    SubcommandName,
    V2BaseCommand,
    convert_argument,
)

from .argument import V2Argument

if TYPE_CHECKING:
    from . import V2Command


class V2PositionalArgumentsCommand(V2BaseCommand):
    arguments: Annotated[
        OrderedDict[Position | Literal["*"] | Keyword, InputArgument | None],
        Field(
            title="arguments of the command.",
            description=(
                "argment key allow "
                "positional integer (like 1, 2), "
                'keyword string (like "--f", "-f"), '
                'wildcard string ("*").'
            ),
        ),
    ]

    @property
    @override
    def subcommands(self) -> OrderedDict[SubcommandName, "V2Command"]:
        return OrderedDict()

    @cached_property
    @override
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict(
            [
                (k, convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, int)
            ]
        )

    @cached_property
    @override
    def positional_wildcard_argument(self) -> V2Argument | None:
        if "*" in self.arguments:
            return convert_argument(self.arguments["*"])
        else:
            return None

    @cached_property
    @override
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, str) and k != "*"
            ]
        )

    @property
    @override
    def has_subcommands(self) -> bool:
        return False

    @property
    @override
    def has_positional_arguments(self) -> bool:
        return len(self.positional_arguments) != 0

    @property
    @override
    def has_positional_wildcard_argument(self) -> bool:
        return self.positional_wildcard_argument is not None

    @property
    @override
    def has_keyword_arguments(self) -> bool:
        return len(self.keyword_arguments) != 0
