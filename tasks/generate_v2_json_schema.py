import json

from cmdcomp.v2.config import V2Config

if __name__ == "__main__":
    print(
        json.dumps(
            V2Config.model_json_schema(),
            indent=4,
        )
    )
