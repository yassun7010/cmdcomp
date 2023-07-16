from pydantic import ConfigDict

from cmdcomp.model import Model
from cmdcomp.v1_config.app_info import AppInfo
from cmdcomp.v1_config.cmdcomp_info import CmdCompInfo
from cmdcomp.v1_config.command.command import Command


class V1Config(Model):
    """cmdcomp config."""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    cmdcomp: CmdCompInfo
    app: AppInfo
    root: Command
