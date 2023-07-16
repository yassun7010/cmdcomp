from cmdcomp.v2.command.argument.command_argument import V2CommandArgument
from cmdcomp.v2.command.argument.file_argument import V2FileArgument
from cmdcomp.v2.command.argument.values_argument import V2ValuesArgument

V2Argument = V2ValuesArgument | V2FileArgument | V2CommandArgument
