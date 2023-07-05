from typing import Annotated, Literal

from pydantic import BaseModel, Field


class CmdCompInfo(BaseModel):
    """cmdcomp info."""

    version: Annotated[
        Literal["1"],
        Field(title="cmdcomp config schema version."),
    ]

    repository: Annotated[
        Literal["https://github.com/yassun4dev/cmdcomp"],
        Field(title="cmdcomp repository url."),
    ]
