`app` describes the settings for the cli app for which the completion file is to
be created.

The complete configuration items are as follows.

=== "yaml"

    ```yaml
    --8<-- "docs/data/v2_app_info/v2_app_info.yaml"
    ```

=== "toml"

    ```toml
    --8<-- "docs/data/v2_app_info/v2_app_info.toml"
    ```

| Property | Required | Type  | Description   |
| -------- | -------- | ----- | ------------- |
| name     | ✅       | `str` | cli app name. |
| alias    |          | `str  | list[str]     |
