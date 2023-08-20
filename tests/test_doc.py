from collections import OrderedDict

import pytest

from cmdcomp import config, model
from cmdcomp.app import App
from cmdcomp.v2.app_info import V2AppInfo
from cmdcomp.v2.command import V2PoristionalArgumentsCommand, V2SubcommandsCommand
from cmdcomp.v2.command.argument.file_argument import V2FileArgument
from tests.conftest import DATA_DIR


class TestAppHelp:
    def test_write_help_to_docs(self, capsys: pytest.CaptureFixture) -> None:
        with pytest.raises(SystemExit):
            App().run(["--help"])

        with open(DATA_DIR / "help.txt", "w") as file:
            file.write(capsys.readouterr().out)

    def test_v2_config(self):
        with open(DATA_DIR / "jinja" / "v2_config_structure.yaml.jinja", "rb") as file:
            config.load(
                file,
                App=(
                    V2AppInfo(
                        name="mycli",
                    ).model_dump_json(indent=2)
                ),
                Command=(
                    V2SubcommandsCommand(
                        arguments=OrderedDict(),
                    ).model_dump_json(indent=2)
                ),
            )

    def test_v2_positional_arguments_command(self):
        with open(
            DATA_DIR / "jinja" / "v2_positional_arguments_command_structure.yaml.jinja",
            "r",
        ) as file:
            model.load(
                V2PoristionalArgumentsCommand,
                file,
                Argument=(
                    V2FileArgument(
                        type="file",
                    ).model_dump_json()
                ),
            )

    def test_v2_subcommands_command(self):
        with open(
            DATA_DIR / "jinja" / "v2_subcommands_command_structure.yaml.jinja",
            "r",
        ) as file:
            model.load(
                V2SubcommandsCommand,
                file,
                Argument=(
                    V2FileArgument(
                        type="file",
                    ).model_dump_json()
                ),
                Command=(
                    V2PoristionalArgumentsCommand(
                        arguments=OrderedDict(),
                    ).model_dump_json()
                ),
            )
