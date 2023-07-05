from typing import Annotated

from pydantic import BaseModel, Field


class AppInfo(BaseModel):
    name: Annotated[str, Field(title="your cli app name.")]
