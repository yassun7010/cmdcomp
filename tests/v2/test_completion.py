import yaml

from cmdcomp.shell import ShellType
from cmdcomp.v2.completion import generate_v2
from cmdcomp.v2.config import V2Config
from tests.conftest import SAMPLES_DIR


class TestV2Completion:
    def test_v2_completion(self) -> None:
        with open(SAMPLES_DIR / "v2" / "config.cmdcomp.yaml", "rb") as file:
            config = V2Config.model_validate(yaml.full_load(file))

        with open(SAMPLES_DIR / "v2" / "output.zsh", "w") as file:
            file.write(generate_v2(ShellType.ZSH, config) + "\n")
