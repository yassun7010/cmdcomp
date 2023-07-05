from typing import BinaryIO

import tomllib
from pydantic import BaseModel, ConfigDict

from cmdcomp.config.app_info import AppInfo
from cmdcomp.config.cmdcomp_info import CmdCompInfo
from cmdcomp.config.command.root_command import RootCommand


class Config(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    cmdcomp: CmdCompInfo
    app: AppInfo
    root: RootCommand


def load(file: BinaryIO) -> Config:
    return Config.model_validate(tomllib.load(file))
