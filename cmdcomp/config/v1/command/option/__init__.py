from typing import Literal

from cmdcomp.config.v1.command.option.command_option import CommandOption
from cmdcomp.config.v1.command.option.file_option import FileOption

StrOption = str

OptionType = Literal["command", "file"]

StrOptions = StrOption | list[StrOption]
SpecificOptions = FileOption | CommandOption
Options = StrOptions | SpecificOptions
