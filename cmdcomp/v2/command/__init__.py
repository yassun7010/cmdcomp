from .delegate_command import V2DelegateCommand
from .positional_arguments_command import V2PositionalArgumentsCommand
from .subcommands_command import V2SubcommandsCommand

V2Command = V2PositionalArgumentsCommand | V2SubcommandsCommand | V2DelegateCommand
