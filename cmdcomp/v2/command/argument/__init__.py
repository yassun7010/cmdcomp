from cmdcomp.v2.command.argument.normal_argument import V2NormalArgument

from .file_argument import V2FileArgument

V2Argument = V2NormalArgument | V2FileArgument
