# Command Completion Generator Tool

<p align="center">
    <a href="https://github.com/yassun4dev/cmdcomp/actions">
        <img src="https://github.com/yassun4dev/cmdcomp/actions/workflows/test-suite.yml/badge.svg" alt="Test Suite">
    </a>
    <a href="https://pypi.org/project/cmdcomp/">
        <img src="https://badge.fury.io/py/cmdcomp.svg" alt="Package version">
    </a>
</p>

`cmdcomp` generate shell completion file (bash or zsh) from config toml file.

## Install

```shell
pip install cmdcomp
```

## Usage

### Local
```shell
cmdcomp --file ${YOUR_CONFIG_TOML_FILE} --shell-type bash
```

### Docker

```shell
docker run --rm -itv $(pwd):/apps/cmdcomp yassun4dev/cmdcomp --file ${YOUR_CONFIG_TOML_FILE} --shell-type bash
```

## JSON Schema

### Config

https://raw.githubusercontent.com/yassun4dev/cmdcomp/main/docs/config.schema.json
