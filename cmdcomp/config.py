import json
import os
import tomllib
from typing import BinaryIO

import yaml
from pydantic import RootModel

from cmdcomp.v1_config.v1_config import V1Config


class Config(RootModel):
    """cmdcomp config."""

    root: V1Config


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
