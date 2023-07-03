from typing import Annotated, Literal

from pydantic import Field


class CmdCompInfo:
    """
    cmdcomp info.
    """

    repository: Annotated[
        Literal["https://github.com/yassun4dev/cmdcomp"],
        Field(title="cmdcomp repository url."),
    ]

    version: Annotated[
        Literal["1.0"],
        Field(title="cmdcomp config schema version."),
    ]
