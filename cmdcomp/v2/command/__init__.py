from abc import ABCMeta, abstractmethod
from functools import cached_property
from typing import Annotated, Literal, OrderedDict, TypeAlias

from pydantic import ConfigDict, Field
from typing_extensions import override

from cmdcomp.model import Model
from cmdcomp.v2.command.argument.flag_argument import V2FlagArgument
from cmdcomp.v2.command.argument.select_argument import V2SelectArgument
from cmdcomp.v2.mixin.has_alias import HasAlias

from .argument import V2Argument

Position: TypeAlias = Annotated[int, Field(ge=1)]
Keyword = Annotated[str, Field(pattern=r"^--?[a-zA-Z0-9_-]+$")]
SubcommandName: TypeAlias = str
_InputArgument = str | list[str] | V2Argument


class _V2BaseCommand(HasAlias, Model, metaclass=ABCMeta):
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


class V2PoristionalArgumentsCommand(_V2BaseCommand):
    arguments: Annotated[
        OrderedDict[Position | Literal["*"] | Keyword, _InputArgument | None],
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
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, int)
            ]
        )

    @cached_property
    @override
    def positional_wildcard_argument(self) -> V2Argument | None:
        if "*" in self.arguments:
            return _convert_argument(self.arguments["*"])
        else:
            return None

    @cached_property
    @override
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
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


class V2SubcommandsCommand(_V2BaseCommand):
    arguments: OrderedDict[Keyword, _InputArgument | None] = Field(
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
                (k, _convert_argument(v))
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


V2Command = V2PoristionalArgumentsCommand | V2SubcommandsCommand


def _convert_argument(value: _InputArgument | None) -> V2Argument:
    match value:
        case str():
            return V2SelectArgument(type="select", options=[value])

        case list():
            return V2SelectArgument(
                type="select",
                options=[v for v in value],
            )

        case None:
            return V2FlagArgument(type="flag")

        case _:
            return value
