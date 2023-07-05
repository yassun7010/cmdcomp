from pathlib import Path

from pytest import CaptureFixture

from cmdcomp import __version__
from cmdcomp.app import App

SAMPLES_DIR = Path(__file__).parent.parent / "samples"


def test_bash_sample(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "config.cmdcomp.toml"),
            "--shell-type",
            "bash",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "output.bash").read()


def test_zsh_sample(capsys: CaptureFixture) -> None:
    App.run(
        [
            "--file",
            str(SAMPLES_DIR / "config.cmdcomp.toml"),
            "--shell-type",
            "zsh",
        ]
    )

    assert capsys.readouterr().out == open(SAMPLES_DIR / "output.zsh").read()
