from pytest import CaptureFixture

from cmdcomp.app import App
from tests.conftest import SAMPLES_DIR


def test_sample_toml_bash(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "v1" / "config.cmdcomp.toml"),
            "--shell-type",
            "bash",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "v1" / "output.bash").read()


def test_sample_toml_zsh(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "v1" / "config.cmdcomp.toml"),
            "--shell-type",
            "zsh",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "v1" / "output.zsh").read()


def test_sample_yaml_bash(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "v1" / "config.cmdcomp.yaml"),
            "--shell-type",
            "bash",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "v1" / "output.bash").read()


def test_sample_yaml_zsh(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "v1" / "config.cmdcomp.yaml"),
            "--shell-type",
            "zsh",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "v1" / "output.zsh").read()


def test_sample_output_bash(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "v1" / "config.cmdcomp.yaml"),
            "--shell-type",
            "bash",
            "--output",
            str(SAMPLES_DIR / "v1" / "output.bash"),
        ]
    )


def test_sample_output_zsh(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "v1" / "config.cmdcomp.yaml"),
            "--shell-type",
            "zsh",
            "--output",
            str(SAMPLES_DIR / "v1" / "output.zsh"),
        ]
    )
