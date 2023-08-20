from io import StringIO
from textwrap import dedent

import pytest

from cmdcomp.config import load
from tests.conftest import DATA_DIR


def make_file(filename: str, contents: str) -> StringIO:
    file = StringIO(contents)
    file.name = filename

    return file


class TestConfig:
    def test_jinja(self):
        config = load(
            make_file(
                "config.yaml.jinja",
                dedent(
                    """
                    {%- set app_name = "mycli" -%}
                    cmdcomp:
                        version: "2"
                    app:
                        name: {{ app_name }}
                    root:
                        arguments:
                            --help:
                    """
                ),
            )
        )

        assert config.root.app.name == "mycli"

    @pytest.mark.parametrize("config_file", (DATA_DIR / "config").iterdir())
    def test_config_file(self, config_file):
        with open(config_file, "rb") as file:
            load(file)
