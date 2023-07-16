from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V1CmdCompInfo(Model):
    """cmdcomp info."""

    version: Annotated[
        Literal["1"],
        Field(title="cmdcomp config schema version."),
    ]
