from functools import cached_property
from typing import TYPE_CHECKING, OrderedDict

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


class V2SubcommandsCommand(V2BaseCommand):
    arguments: OrderedDict[Keyword, InputArgument | None] = Field(
        title="arguments of the command.",
        description='argment key allow keyword string (like "--f", "-f") only.',
        default_factory=OrderedDict,
    )

    raw_subcommands: OrderedDict[SubcommandName, "V2Command | None"] = Field(
        title="subcommands of the command.",
        alias="subcommands",
        default_factory=OrderedDict,
    )

    @property
    @override
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict()

    @property
    @override
    def positional_wildcard_argument(self) -> V2Argument | None:
        return None

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

    @cached_property
    @override
    def subcommands(self) -> OrderedDict[SubcommandName, "V2Command"]:
        return OrderedDict(
            [
                (
                    name,
                    V2SubcommandsCommand() if subcommand is None else subcommand,
                )
                for name, subcommand in self.raw_subcommands.items()
            ]
        )

    @property
    @override
    def has_subcommands(self) -> bool:
        return len(self.subcommands) != 0

    @property
    @override
    def has_positional_arguments(self) -> bool:
        return False

    @property
    @override
    def has_positional_wildcard_argument(self) -> bool:
        return self.positional_wildcard_argument is not None

    @property
    @override
    def has_keyword_arguments(self) -> bool:
        return len(self.keyword_arguments) != 0
