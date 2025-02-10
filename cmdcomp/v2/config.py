from pydantic import ConfigDict

from cmdcomp.model import Model

from .app_info import V2AppInfo
from .cmdcomp_info import V2CmdCompInfo
from .command import V2Command


class V2Config(Model):
    """cmdcomp config v2."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    cmdcomp: V2CmdCompInfo
    app: V2AppInfo
    root: V2Command
