---
title: Overview
---

## Run it

```shell title="The simplest example"
cmdcmp --file config.yaml --shell-type bash
```

```shell title="Help"
$ cmdcomp --help
--8<-- "help.txt"
```

## Config

cmdcomp automatically generates a completion file according to the contents of
the configuration file.

The overall structure of the configuration file is shown below.

```yaml
--8<-- "jinja/v2_config_structure.yaml.jinja"
```

More detailed information is given in the next section.

Please refer to
[JSON Schema](https://raw.githubusercontent.com/yassun7010/cmdcomp/main/docs/config.schema.json)
for exact schema information.

!!! tip

    You can use `json` `yaml` `toml` for the format of the config file, but I recommend `yaml` for configuration.

    The [yaml language server](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) gives 
    the best development experience as an extension available for VSCode.

    I have added the following configuration to VSCode, which makes it easier to write configuration files.

    ```json title=".vscode/settings.json"
    {
        "yaml.schemas": {
            "https://raw.githubusercontent.com/yassun7010/cmdcomp/main/docs/config.schema.json": "*_cmdcomp.yaml"
        },
    }
    ```
