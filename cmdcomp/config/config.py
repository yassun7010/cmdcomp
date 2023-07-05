import json
import os
from typing import BinaryIO

import tomllib
import yaml
from pydantic import BaseModel, ConfigDict

from cmdcomp.config.app_info import AppInfo
from cmdcomp.config.cmdcomp_info import CmdCompInfo
from cmdcomp.config.command.command import Command


class Config(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    cmdcomp: CmdCompInfo
    app: AppInfo
    root: Command


def load(file: BinaryIO) -> Config:
    _, extention = os.path.splitext(file.name)
    match extention:
        case ".json":
            data = json.load(file)
        case ".yaml":
            data = yaml.full_load(file)
        case ".toml":
            data = tomllib.load(file)
        case _:
            raise Exception(f"Unsupported config file type `{extention}`.")

    return Config.model_validate(data)
