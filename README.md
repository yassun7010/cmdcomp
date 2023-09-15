# Command Completion Generator Tool

<!-- --8<-- [start:badges] -->

[![docs](https://github.com/yassun7010/cmdcomp/actions/workflows/publish-mkdocs.yml/badge.svg)](https://yassun7010.github.io/cmdcomp/)
[![test](https://github.com/yassun7010/cmdcomp/actions/workflows/test-suite.yml/badge.svg)](https://github.com/yassun7010/cmdcomp/actions)
[![pypi package](https://badge.fury.io/py/cmdcomp.svg)](https://pypi.org/project/cmdcomp)
[![docker version](https://img.shields.io/docker/v/yassun7010/cmdcomp/latest?label=docker%20version)](https://hub.docker.com/r/yassun7010/cmdcomp)

<!-- --8<-- [end:badges] -->

`cmdcomp` generate command shell completion file (`bash` or `zsh`) from config
`json`/`yaml`/`toml` file.

![image](./images/image.png)

## Install

```shell
pip install cmdcomp
```

## Usage

```shell
cmdcomp --file $YOUR_CONFIG_FILE --shell-type bash
```

## Documentation

See [documentation](https://yassun7010.github.io/cmdcomp/) for more details.

## Examples

See [examples](https://github.com/yassun7010/cmdcomp/tree/main/examples/v2).
