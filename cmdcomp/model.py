import json
import os
import tomllib
from io import StringIO
from typing import IO, Type, TypeVar

import jinja2
import yaml
from pydantic import BaseModel, ConfigDict

from cmdcomp.exception import FileExtensionError

T = TypeVar("T", bound=BaseModel)


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


def load(type: Type[T], file: IO, **kwargs) -> T:
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

            rendered_file = StringIO(jinja2.Template(data).render(os.environ, **kwargs))
            rendered_file.name = root

            return load(type, rendered_file, **kwargs)

        case _:
            raise FileExtensionError(file.name, extension)

    return type.model_validate(config)
