from cmdcomp.config import Config
from cmdcomp.shell import ShellType
from cmdcomp.v1_config.completion import generate_v1
from cmdcomp.v1_config.v1_config import V1Config


def generate(shell: ShellType, config: Config) -> str:
    match config.root:
        case V1Config():
            return generate_v1(shell, config.root)
