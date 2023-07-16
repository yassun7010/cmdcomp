import tomllib

from cmdcomp.v2.config import V2Config


class TestV2Config:
    def test_v2_config(self) -> None:
        data = tomllib.loads(
            """
            [cmdcomp]
            version = "2"

            [app]
            name = "cliname"
            alias = "clialias"
            """
        )
        V2Config.model_validate(data)
