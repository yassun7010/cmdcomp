from typing import Literal

from cmdcomp.v1.command.option.command_option import V1CommandOption
from cmdcomp.v1.command.option.file_option import V1FileOption

V1StrOption = str

V1OptionType = Literal["command", "file"]

V1SpecificOptions = V1FileOption | V1CommandOption
V1Options = V1StrOption | list[V1StrOption] | V1SpecificOptions
