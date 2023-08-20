`app` describes the settings for the cli app for which the completion file is to
be created.

The complete configuration items are as follows.

=== "yaml"

    ```yaml
    --8<- "v2_app_info/v2_app_info.yaml"
    ```

=== "toml"

    ```toml
    --8<- "v2_app_info/v2_app_info.toml"
    ```

| Property | Type                    | Description     |
| -------- | ----------------------- | --------------- |
| name     | `str`                   | cli app name.   |
| alias    | `Union[str, list[str]]` | app name alias. |
