from pathlib import Path

from pytest import CaptureFixture

from cmdcomp.app import App

SAMPLES_DIR = Path(__file__).parent.parent / "samples"


def test_sample_toml_bash(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "config.cmdcomp.toml"),
            "--shell-type",
            "bash",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "output.bash").read()


def test_sample_toml_zsh(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "config.cmdcomp.toml"),
            "--shell-type",
            "zsh",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "output.zsh").read()


def test_sample_yaml_bash(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "config.cmdcomp.yaml"),
            "--shell-type",
            "bash",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "output.bash").read()


def test_sample_yaml_zsh(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "config.cmdcomp.yaml"),
            "--shell-type",
            "zsh",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "output.zsh").read()
