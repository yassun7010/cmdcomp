from pydantic import BaseModel

from cmdcomp.config.cmdcomp_info import CmdCompInfo


class Config(BaseModel):
    cmdcomp: CmdCompInfo
