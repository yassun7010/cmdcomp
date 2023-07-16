from typing import Literal

from cmdcomp.v1_config.v1_command.v1_option.v1_command_option import V1CommandOption
from cmdcomp.v1_config.v1_command.v1_option.v1_file_option import V1FileOption

V1StrOption = str

V1OptionType = Literal["command", "file"]

V1StrOptions = V1StrOption | list[V1StrOption]
V1SpecificOptions = V1FileOption | V1CommandOption
V1Options = V1StrOptions | V1SpecificOptions
