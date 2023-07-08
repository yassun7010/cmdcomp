# Command Completion Generator Tool

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
