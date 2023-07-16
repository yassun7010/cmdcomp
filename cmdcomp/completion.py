from cmdcomp.config import Config
from cmdcomp.shell import ShellType
from cmdcomp.v1_config.completion import generate_v1


def generate(shell: ShellType, config: Config):
    return generate_v1(shell, config.root)
