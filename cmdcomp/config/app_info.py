from typing import Annotated

from pydantic import Field

from cmdcomp.config.model import Model


class AppInfo(Model):
    name: Annotated[str, Field(title="your cli app name.")]
