from typing import assert_never

from cmdcomp.config import Config
from cmdcomp.shell import ShellType
from cmdcomp.v1.completion import generate_v1
from cmdcomp.v1.config import V1Config
from cmdcomp.v2.completion import generate_v2
from cmdcomp.v2.config import V2Config


def generate(shell: ShellType, config: Config) -> str:
    match config.root:
        case V1Config():
            return generate_v1(shell, config.root)

        case V2Config():
            return generate_v2(shell, config.root)

        case _:
            assert_never(config.root)
