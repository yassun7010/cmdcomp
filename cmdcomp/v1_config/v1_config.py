from pydantic import ConfigDict

from cmdcomp.model import Model
from cmdcomp.v1_config.v1_app_info import V1AppInfo
from cmdcomp.v1_config.v1_cmdcomp_info import V1CmdCompInfo
from cmdcomp.v1_config.v1_command.v1_command import V1Command


class V1Config(Model):
    """cmdcomp config."""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    cmdcomp: V1CmdCompInfo
    app: V1AppInfo
    root: V1Command
