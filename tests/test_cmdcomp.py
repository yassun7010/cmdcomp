import pytest
from pytest import CaptureFixture

from cmdcomp.app import App
from cmdcomp.shell import ShellType
from tests.conftest import SAMPLES_DIR


@pytest.mark.parametrize("version", ["v1", "v2"])
@pytest.mark.parametrize("config_format", ["yaml", "toml"])
@pytest.mark.parametrize("shell", ShellType)
class TestApplication:
    def test_application(
        self,
        capsys: CaptureFixture,
        version: str,
        config_format: str,
        shell: ShellType,
    ) -> None:
        App.run(
            [
                "--file",
                str(SAMPLES_DIR / version / f"config.cmdcomp.{config_format}"),
                "--shell-type",
                shell.value,
            ]
        )

        assert (
            capsys.readouterr().out
            == open(SAMPLES_DIR / version / f"output.{str(shell.value)}").read()
        )

    def test_output_file_to_samples(
        self,
        version: str,
        config_format: str,
        shell: ShellType,
    ) -> None:
        App.run(
            [
                "--file",
                str(SAMPLES_DIR / version / f"config.cmdcomp.{config_format}"),
                "--shell-type",
                shell.value,
                "--output",
                str(SAMPLES_DIR / version / f"output.{shell.value}"),
            ]
        )
