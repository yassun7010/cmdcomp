from collections import OrderedDict

import pytest

from cmdcomp import config
from cmdcomp.app import App
from cmdcomp.v2.app_info import V2AppInfo
from cmdcomp.v2.command import V2SubcommandsCommand
from tests.conftest import DATA_DIR


class TestAppHelp:
    def test_write_help_to_docs(self, capsys: pytest.CaptureFixture) -> None:
        with pytest.raises(SystemExit):
            App().run(["--help"])

        with open(DATA_DIR / "help.txt", "w") as file:
            file.write(capsys.readouterr().out)

    def test_v2_config(self):
        with open(
            DATA_DIR / "config_jinja" / "v2_config_structure.yaml.jinja", "rb"
        ) as file:
            config.load(
                file,
                App=(
                    V2AppInfo(
                        name="mycli",
                        alias="my-cli",
                    ).model_dump_json(indent=2)
                ),
                Command=(
                    V2SubcommandsCommand(
                        alias=None,
                        arguments=OrderedDict(),
                    ).model_dump_json(indent=2)
                ),
            )
