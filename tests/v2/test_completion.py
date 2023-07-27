import yaml

from cmdcomp.shell import ShellType
from cmdcomp.v2.completion import generate_v2
from cmdcomp.v2.config import V2Config
from tests.conftest import SAMPLES_DIR


class TestV2Completion:
    def test_v2_bash_completion(self) -> None:
        with (
            open(SAMPLES_DIR / "v2" / "config.cmdcomp.yaml", "rb") as read_file,
            open(SAMPLES_DIR / "v2" / "output.bash", "w") as write_file,
        ):
            config = V2Config.model_validate(yaml.full_load(read_file))
            write_file.write(generate_v2(ShellType.BASH, config) + "\n")

    def test_v2_zsh_completion(self) -> None:
        with (
            open(SAMPLES_DIR / "v2" / "config.cmdcomp.yaml", "rb") as read_file,
            open(SAMPLES_DIR / "v2" / "output.zsh", "w") as write_file,
        ):
            config = V2Config.model_validate(yaml.full_load(read_file))
            write_file.write(generate_v2(ShellType.ZSH, config) + "\n")
