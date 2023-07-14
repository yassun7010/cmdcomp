from enum import Enum


class ShellType(Enum):
    BASH = "bash"
    ZSH = "zsh"

    def __str__(self):
        return self.value
