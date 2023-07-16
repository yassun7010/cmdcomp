from pydantic import ConfigDict

from cmdcomp.model import Model
from cmdcomp.v1.app_info import V1AppInfo
from cmdcomp.v1.cmdcomp_info import V1CmdCompInfo
from cmdcomp.v1.command import V1Command


class V1Config(Model):
    """cmdcomp config."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    cmdcomp: V1CmdCompInfo
    app: V1AppInfo
    root: V1Command
