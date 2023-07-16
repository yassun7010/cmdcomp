from cmdcomp.v2.command.argument.command_argument import V2CommandArgument
from cmdcomp.v2.command.argument.file_argument import V2FileArgument
from cmdcomp.v2.command.argument.normal_argument import V2NormalArgument

V2Argument = V2NormalArgument | V2FileArgument | V2CommandArgument
