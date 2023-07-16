from collections import OrderedDict
from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.exception import NeverReach
from cmdcomp.model import Model


class V2ValueArgument(Model):
    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    value: Annotated[
        str,
        Field(title="value of the argument."),
    ]


class V2ValuesArgument(Model):
    type: Literal["values"] | None = None

    description: str | None = Field(
        title="description of the argument.",
        default=None,
    )

    candidates__: Annotated[
        str | list[str] | OrderedDict[str, str | V2ValueArgument],
        Field(
            title="values of the argument.",
            alias="candidates",
        ),
    ]

    @property
    def candidates(self) -> OrderedDict[str, V2ValueArgument]:
        match self.candidates__:
            case str():
                return OrderedDict(
                    [(self.candidates__, V2ValueArgument(value=self.candidates__))]
                )

            case list():
                return OrderedDict(
                    [(v, V2ValueArgument(value=v)) for v in self.candidates__]
                )

            case OrderedDict():
                return OrderedDict(
                    [
                        (
                            k,
                            v
                            if isinstance(v, V2ValueArgument)
                            else V2ValueArgument(value=v),
                        )
                        for k, v in self.candidates__.items()
                    ]
                )

            case _:
                raise NeverReach(self.candidates__)
