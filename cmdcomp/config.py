import json
import os
import tomllib
from io import StringIO
from typing import IO

import jinja2
import yaml
from pydantic import RootModel

from cmdcomp.exception import ConfigFileExtensionError
from cmdcomp.v1.config import V1Config
from cmdcomp.v2.config import V2Config


class Config(RootModel):
    """cmdcomp config."""

    root: V1Config | V2Config


def load(file: IO) -> Config:
    root, extension = os.path.splitext(file.name)
    match extension:
        case ".json":
            data = json.load(file)

        case ".yaml" | ".yml":
            data = yaml.full_load(file)

        case ".toml":
            data = tomllib.load(file)

        case ".jinja" | "jinja2" | ".j2":
            data = StringIO(jinja2.Template(file.read()).render(os.environ))
            data.name = root

            return load(data)

        case _:
            raise ConfigFileExtensionError(extension)

    return Config.model_validate(data)
