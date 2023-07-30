import json
import os
import tomllib
from typing import BinaryIO

import yaml
from pydantic import RootModel

from cmdcomp.exception import ConfigFileExtensionError
from cmdcomp.v1.config import V1Config
from cmdcomp.v2.config import V2Config


class Config(RootModel):
    """cmdcomp config."""

    root: V1Config | V2Config


def load(file: BinaryIO) -> Config:
    _, extension = os.path.splitext(file.name)
    match extension:
        case ".json":
            data = json.load(file)

        case ".yaml" | ".yml":
            data = yaml.full_load(file)

        case ".toml":
            data = tomllib.load(file)

        case _:
            raise ConfigFileExtensionError(extension)

    return Config.model_validate(data)
