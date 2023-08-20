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


def load(file: IO, **kwargs) -> Config:
    root, extension = os.path.splitext(file.name)
    match extension:
        case ".json":
            config = json.load(file)

        case ".yaml" | ".yml":
            config = yaml.full_load(file)

        case ".toml":
            config = tomllib.load(file)

        case ".jinja" | "jinja2" | ".j2":
            data: bytes | str = file.read()
            if isinstance(data, bytes):
                data = data.decode("utf-8")

            file = StringIO(jinja2.Template(data).render(os.environ, **kwargs))
            file.name = root

            return load(file)

        case _:
            raise ConfigFileExtensionError(extension)

    return Config.model_validate(config)
