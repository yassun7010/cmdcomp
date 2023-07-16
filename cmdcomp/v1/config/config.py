import json
import os
import tomllib
from typing import BinaryIO

import yaml
from pydantic import ConfigDict

from cmdcomp.v1.config.app_info import AppInfo
from cmdcomp.v1.config.cmdcomp_info import CmdCompInfo
from cmdcomp.v1.config.command.command import Command
from cmdcomp.v1.config.model import Model


class Config(Model):
    """cmdcomp config."""

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    cmdcomp: CmdCompInfo
    app: AppInfo
    root: Command


def load(file: BinaryIO) -> Config:
    _, extention = os.path.splitext(file.name)
    match extention:
        case ".json":
            data = json.load(file)
        case ".yaml" | ".yml":
            data = yaml.full_load(file)
        case ".toml":
            data = tomllib.load(file)
        case _:
            raise Exception(f"Unsupported config file type `{extention}`.")

    return Config.model_validate(data)
