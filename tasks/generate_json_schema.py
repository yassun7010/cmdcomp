import json

from cmdcomp.v1.config.config import Config

if __name__ == "__main__":
    print(
        json.dumps(
            Config.model_json_schema(),
            indent=4,
        )
    )
