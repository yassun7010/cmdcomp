# Command Completion Generator Tool

<!-- --8<-- [start:badges] -->
[![docs](https://github.com/yassun7010/cmdcomp/actions/workflows/publish-mkdocs.yml/badge.svg)](https://yassun7010.github.io/cmdcomp/)
[![test](https://github.com/yassun7010/cmdcomp/actions/workflows/test-suite.yml/badge.svg)](https://github.com/yassun7010/cmdcomp/actions)
[![pypi](https://badge.fury.io/py/cmdcomp.svg)](https://pypi.org/project/cmdcomp)
[![docker](https://img.shields.io/docker/v/yassun7010/cmdcomp/latest?label=docker%20version)](https://hub.docker.com/r/yassun7010/cmdcomp)
<!-- --8<-- [end:badges] -->


`cmdcomp` generate command shell completion file (`bash` or `zsh`) from config
`json`/`yaml`/`toml` file.

## Install

```shell
pip install cmdcomp
```

## Help

See [documentation](https://yassun7010.github.io/cmdcomp/) for more details.

## Usage

### Local

```shell
cmdcomp --file ${YOUR_CONFIG_FILE} --shell-type bash
```

### Docker

```shell
docker run --rm -itv $(pwd):/app/cmdcomp yassun7010/cmdcomp --file ${YOUR_CONFIG_FILE} --shell-type bash
```

## Config

Configuration can be written in `JSON`, `YAML`, and `TOML` file formats.

### Sample

```yaml
cmdcomp:
  version: "2"
app:
  name: "mycli"
  alias: "my-cli"
root:
  arguments:
    --verbose:
      type: flag
      description: "verbose output."
    --no-verbose:
      type: flag
      description: "no verbose output."
    --version:
      type: flag
      alias: "-V"
      description: "print version."
    --config:
      type: file
      description: "config file."
    --type:
      type: select
      description: "config file type."
      values:
        - json
        - toml
    --help:
      type: flag
      description: "print help."
  subcommands:
    list:
      alias: "ls"
      description: "list project files."
      arguments:
        --all:
          type: flag
          alias: "-a"
          description: "list all files."
        "*":
          type: file
          description: "list files."
    cd:
      description: "cd project directory."
      arguments:
        -P:
          type: flag
          description: "physical directory."
        1:
          type: file
          base_path: $HOME
          description: "change home directory."
    test:
      description: "test command."
      subcommands:
        rubocop:
          description: "run rubocop."
          arguments:
            --auto-correct:
              type: flag
              alias: "-A"
              description: "auto correct."
        pytest:
          description: "run pytest."
```

### JSON Schema

https://raw.githubusercontent.com/yassun7010/cmdcomp/main/docs/config.schema.json
