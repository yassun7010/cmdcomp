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

`cmdcomp` generate shell completion file (bash or zsh) from config yaml/toml file.

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

Configuration can be written in JSON, YAML, and TOML file formats.

### Sample

```toml
[cmdcomp]
version = "1"

[app]
name = "mycli"
alias = "my-cli"

[root]
options = ["-h", "--help", "--version"]

[root.subcommands.list]
options = ["-a"]
alias = "ls"

[root.subcommands.execute]
options = { type = "command", execute = "your_app_name ps -s" }
alias = ["restart", "shell", "log"]

[root.subcommands.cd]
options = { type = "file", base_path = "$(cd $(dirname $0); pwd)/../apps" }

```

### JSON Schema

https://raw.githubusercontent.com/yassun4dev/cmdcomp/main/docs/config.schema.json
