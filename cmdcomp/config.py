from typing import IO

from pydantic import RootModel

from cmdcomp import model
from cmdcomp.v1.config import V1Config
from cmdcomp.v2.config import V2Config


class Config(RootModel):
    """cmdcomp config."""

    root: V1Config | V2Config


def load(file: IO, **kwargs) -> Config:
    return model.load(Config, file, **kwargs)
