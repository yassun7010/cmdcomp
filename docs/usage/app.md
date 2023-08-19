`app` describes the settings for the cli app for which the completion file is to
be created.

The complete configuration items are as follows.

=== "yaml"

    ```yaml
    app:
      name: mycli
      alias: my-cli
    ```

=== "toml"

    ```toml
    [app]
    name = "mycli"
    alias = "my-cli"
    ```

| Property | Type                    | Description     |
| -------- | ----------------------- | --------------- |
| name     | `str`                   | cli app name.   |
| alias    | `Union[str, list[str]]` | app name alias. |
