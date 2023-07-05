from typing import Annotated

from pydantic import Field

from cmdcomp.config.model import Model


class AppInfo(Model):
    """your cli app info."""

    name: Annotated[str, Field(title="your cli app name.")]
