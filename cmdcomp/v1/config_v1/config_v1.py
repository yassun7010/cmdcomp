from pydantic import ConfigDict

from cmdcomp.v1.config_v1.app_info import AppInfo
from cmdcomp.v1.config_v1.cmdcomp_info import CmdCompInfo
from cmdcomp.v1.config_v1.command.command import Command
from cmdcomp.v1.config_v1.model import Model


class ConfigV1(Model):
    """cmdcomp config."""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    cmdcomp: CmdCompInfo
    app: AppInfo
    root: Command
