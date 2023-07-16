from pydantic import ConfigDict

from cmdcomp.model import Model
from cmdcomp.v2.app_info import V2AppInfo
from cmdcomp.v2.cmdcomp_info import V2CmdCompInfo
from cmdcomp.v2.command import V2Command


class V2Config(Model):
    """cmdcomp config v2."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    cmdcomp: V2CmdCompInfo
    app: V2AppInfo
    root: V2Command
