from typing import Literal

from cmdcomp.v1_config.command.option.command_option import CommandOption
from cmdcomp.v1_config.command.option.file_option import FileOption

StrOption = str

OptionType = Literal["command", "file"]

StrOptions = StrOption | list[StrOption]
SpecificOptions = FileOption | CommandOption
Options = StrOptions | SpecificOptions
