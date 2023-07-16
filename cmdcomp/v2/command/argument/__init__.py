from cmdcomp.v2.command.argument.str_argument import V2StrArgument

from .file_argument import V2FileArgument

V2Argument = V2StrArgument | list[V2StrArgument] | V2FileArgument
