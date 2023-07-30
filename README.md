# Command Completion Generator Tool

<p align="center">
    <a href="https://github.com/yassun4dev/cmdcomp/actions">
        <img src="https://github.com/yassun4dev/cmdcomp/actions/workflows/test-suite.yml/badge.svg" alt="Test Suite">
    </a>
    <a href="https://pypi.org/project/cmdcomp">
        <img src="https://badge.fury.io/py/cmdcomp.svg" alt="PIP Version">
    </a>
    <a href="https://hub.docker.com/r/yassun4dev/cmdcomp">
        <img src="https://img.shields.io/docker/v/yassun4dev/cmdcomp/latest?label=docker%20version" alt="Docker Version">
    </a>
</p>

`cmdcomp` generate shell completion file (`bash` or `zsh`) from config `json`/`yaml`/`toml` file.

## Install

```shell
pip install cmdcomp
```

## Usage

### Local
```shell
cmdcomp --file ${YOUR_CONFIG_FILE} --shell-type bash
```

### Docker

```shell
docker run --rm -itv $(pwd):/app/cmdcomp yassun4dev/cmdcomp --file ${YOUR_CONFIG_FILE} --shell-type bash
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
          description: "change project directory."
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

https://raw.githubusercontent.com/yassun4dev/cmdcomp/main/docs/config.schema.json
