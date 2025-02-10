from typing import IO

from pydantic import RootModel

from cmdcomp import model

from .v1.config import V1Config
from .v2.config import V2Config


class Config(RootModel):
    """cmdcomp config."""

    root: V1Config | V2Config


def load(file: IO, **kwargs) -> Config:
    return model.load(Config, file, **kwargs)
