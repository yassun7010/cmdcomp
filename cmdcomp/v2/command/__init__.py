from typing import Annotated, Literal, OrderedDict, TypeAlias

from pydantic import ConfigDict, Field

from cmdcomp.model import Model
from cmdcomp.v2.command.argument.command_argument import V2CommandArgument
from cmdcomp.v2.command.argument.file_argument import V2FileArgument
from cmdcomp.v2.command.argument.flag_argument import V2FlagArgument
from cmdcomp.v2.command.argument.values_argument import (
    V2ValueArgument,
    V2ValuesArgument,
)

from .argument import V2Argument

Position: TypeAlias = Annotated[int, Field(ge=1)]
Keyword = Annotated[str, Field(pattern=r"^--?[a-zA-Z0-9_-]+$")]
SubcommandName: TypeAlias = str


class V2PoristionalArgumentsCommand(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    description: str | None = Field(
        title="description of the command.",
        default=None,
    )

    arguments: Annotated[
        OrderedDict[
            Position | Literal["*"] | Keyword,
            str
            | list[str]
            | V2ValuesArgument
            | V2FileArgument
            | V2CommandArgument
            | V2FlagArgument
            | None,
        ],
        Field(
            title="arguments of the command.",
            description=(
                "argment key allow "
                "positional integer (like `1` , `2`), "
                'keyword string(like `"--f"`, `"-f"`), '
                'wildcard string(`"*"`).'
            ),
        ),
    ]

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias

    @property
    def subcommands(self) -> OrderedDict[SubcommandName, "V2Command"]:
        return OrderedDict()

    @property
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, int)
            ]
        )

    @property
    def positional_wildcard_argument(self) -> V2Argument | None:
        if "*" in self.arguments:
            return _convert_argument(self.arguments["*"])
        else:
            return None

    @property
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, str) and k != "*"
            ]
        )

    @property
    def subcommand_names_with_alias(self) -> list[SubcommandName]:
        return _subcommand_names_with_alias(self)

    @property
    def keyword_names_with_alias(self) -> list[Keyword]:
        return _keyword_names_with_alias(self)

    @property
    def has_subcommands(self) -> bool:
        return False

    @property
    def has_positional_arguments(self) -> bool:
        return len(self.positional_arguments) != 0

    @property
    def has_positional_wildcard_argument(self) -> bool:
        return self.positional_wildcard_argument is not None

    @property
    def has_keyword_arguments(self) -> bool:
        return len(self.keyword_arguments) != 0


class V2SubcommandsCommand(Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: str | None = Field(
        title="description of the command.",
        default=None,
    )

    alias: Annotated[
        str | list[str],
        Field(
            title="alias of the command.",
            default_factory=list,
        ),
    ]

    arguments: Annotated[
        OrderedDict[
            Keyword,
            str
            | list[str]
            | V2ValuesArgument
            | V2FileArgument
            | V2CommandArgument
            | V2FlagArgument
            | None,
        ],
        Field(
            title="arguments of the command.",
            description='argment key allow keyword string (like "--f", "-f") only.',
            default_factory=OrderedDict,
        ),
    ]

    subcommands: OrderedDict[SubcommandName, "V2Command"] = Field(
        title="subcommands of the command.",
        default_factory=OrderedDict,
    )

    @property
    def aliases(self) -> list[str]:
        if isinstance(self.alias, str):
            return [self.alias]
        else:
            return self.alias

    @property
    def positional_arguments(self) -> OrderedDict[Position, V2Argument]:
        return OrderedDict()

    @property
    def positional_wildcard_argument(self) -> V2Argument | None:
        return None

    @property
    def keyword_arguments(self) -> OrderedDict[Keyword, V2Argument]:
        return OrderedDict(
            [
                (k, _convert_argument(v))
                for k, v in self.arguments.items()
                if isinstance(k, str)
            ]
        )

    @property
    def subcommand_names_with_alias(self) -> list[SubcommandName]:
        return _subcommand_names_with_alias(self)

    @property
    def keyword_names_with_alias(self) -> list[Keyword]:
        return _keyword_names_with_alias(self)

    @property
    def has_subcommands(self) -> bool:
        return len(self.subcommands) != 0

    @property
    def has_positional_arguments(self) -> bool:
        return False

    @property
    def has_positional_wildcard_argument(self) -> bool:
        return self.positional_wildcard_argument is not None

    @property
    def has_keyword_arguments(self) -> bool:
        return len(self.keyword_arguments) != 0


V2Command = V2PoristionalArgumentsCommand | V2SubcommandsCommand


def _convert_argument(
    value: str
    | list[str]
    | V2ValuesArgument
    | V2FileArgument
    | V2CommandArgument
    | V2FlagArgument
    | None,
) -> V2Argument:
    match value:
        case str():
            return V2ValuesArgument(type="values", values=[value])

        case list():
            return V2ValuesArgument(
                type="values",
                values=[V2ValueArgument(value=v) for v in value],
            )

        case None:
            return V2FlagArgument(type="flag")

        case _:
            return value


def _subcommand_names_with_alias(command: V2Command) -> list[SubcommandName]:
    result: list[SubcommandName] = []
    for subcommand_name, subcommand in command.subcommands.items():
        result.append(subcommand_name)
        result.extend(subcommand.aliases)

    return result


def _keyword_names_with_alias(command: V2Command) -> list[Keyword]:
    result: list[Keyword] = []
    for keyword, argument in command.keyword_arguments.items():
        result.append(keyword)
        result.extend(argument.aliases)

    return result
