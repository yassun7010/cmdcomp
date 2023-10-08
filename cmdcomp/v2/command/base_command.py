from abc import ABCMeta, abstractmethod
from functools import cached_property
from typing import TYPE_CHECKING, Annotated, OrderedDict, TypeAlias

from pydantic import ConfigDict, Field

from cmdcomp.model import Model
from cmdcomp.v2.command.argument.flag_argument import V2FlagArgument
from cmdcomp.v2.command.argument.select_argument import V2SelectArgument
from cmdcomp.v2.mixin.has_alias import HasAlias

from .argument import V2Argument

Position: TypeAlias = Annotated[int, Field(ge=1)]
Keyword = Annotated[str, Field(pattern=r"^--?[a-zA-Z0-9_-]+$")]
SubcommandName: TypeAlias = str
InputArgument = str | list[str] | V2Argument

if TYPE_CHECKING:
    from . import V2Command


class V2BaseCommand(HasAlias, Model, metaclass=ABCMeta):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: Annotated[
        str | None,
        Field(title="description of the command."),
    ] = None

    alias: Annotated[
        str | list[str] | None,
        Field(title="alias of the command."),
    ] = None

    @cached_property
    def subcommand_names_with_alias(self) -> list[SubcommandName]:
        result: list[SubcommandName] = []
        for subcommand_name, subcommand in self.subcommands.items():
            result.append(subcommand_name)
            result.extend(subcommand.aliases)

        return result

    @cached_property
    def keyword_names_with_alias(self) -> list[Keyword]:
        result: list[Keyword] = []
        for keyword, argument in self.keyword_arguments.items():
            result.append(keyword)
            result.extend(argument.aliases)

        return result

    @property
    @abstractmethod
    def subcommands(self) -> OrderedDict[SubcommandName, "V2Command"]:
        ...

    @property
    @abstractmethod
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        ...

    @property
    @abstractmethod
    def positional_wildcard_argument(self) -> V2Argument | None:
        ...

    @property
    @abstractmethod
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        ...

    @property
    @abstractmethod
    def has_subcommands(self) -> bool:
        ...

    @property
    @abstractmethod
    def has_positional_arguments(self) -> bool:
        ...

    @property
    @abstractmethod
    def has_positional_wildcard_argument(self) -> bool:
        ...

    @property
    @abstractmethod
    def has_keyword_arguments(self) -> bool:
        ...


def convert_argument(value: InputArgument | None) -> V2Argument:
    match value:
        case str():
            return V2SelectArgument(type="select", raw_options=[value])

        case list():
            return V2SelectArgument(
                type="select",
                raw_options=[v for v in value],
            )

        case None:
            return V2FlagArgument(type="flag")

        case _:
            return value
