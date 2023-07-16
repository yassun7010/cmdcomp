from typing import Annotated, Literal

from pydantic import Field

from cmdcomp.v1.v1_config.model import Model


class CmdCompInfo(Model):
    """cmdcomp info."""

    version: Annotated[
        Literal["1"],
        Field(title="cmdcomp config schema version."),
    ]
