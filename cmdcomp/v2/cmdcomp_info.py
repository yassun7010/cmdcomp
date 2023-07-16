from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.model import Model


class V2CmdCompInfo(Model):
    """cmdcomp info."""

    version: Annotated[
        Literal["2"],
        Field(title="cmdcomp config schema version."),
    ]
