from pydantic import BaseModel

from cmdcomp.config.app_info import AppInfo
from cmdcomp.config.cmdcomp_info import CmdCompInfo
from cmdcomp.config.command.root_command import RootCommand


class Config(BaseModel):
    cmdcomp: CmdCompInfo
    app: AppInfo
    root: RootCommand
