from typing import TYPE_CHECKING, OrderedDict

from typing_extensions import override

from .argument import V2Argument
from .base_command import Keyword, Position, SubcommandName, V2BaseCommand

if TYPE_CHECKING:
    from . import V2Command


class V2EmptyCommand(V2BaseCommand):
    @property
    @override
    def subcommands(self) -> OrderedDict[SubcommandName, "V2Command"]:
        return OrderedDict()

    @property
    @override
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict()

    @property
    @override
    def positional_wildcard_argument(self) -> V2Argument | None:
        return None

    @property
    @override
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict()

    @property
    @override
    def has_subcommands(self) -> bool:
        return False

    @property
    @override
    def has_positional_arguments(self) -> bool:
        return False

    @property
    @override
    def has_positional_wildcard_argument(self) -> bool:
        return False

    @property
    @override
    def has_keyword_arguments(self) -> bool:
        return False
