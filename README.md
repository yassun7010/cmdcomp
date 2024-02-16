# Command Completion Generator Tool

<!-- --8<-- [start:badges] -->

[![docs](https://github.com/yassun7010/cmdcomp/actions/workflows/publish-mkdocs.yml/badge.svg)](https://yassun7010.github.io/cmdcomp/)
[![test](https://github.com/yassun7010/cmdcomp/actions/workflows/test-suite.yml/badge.svg)](https://github.com/yassun7010/cmdcomp/actions)
[![pypi package](https://badge.fury.io/py/cmdcomp.svg)](https://pypi.org/project/cmdcomp)
[![docker version](https://img.shields.io/docker/v/yassun7010/cmdcomp/latest?label=docker%20version)](https://hub.docker.com/r/yassun7010/cmdcomp)

<!-- --8<-- [end:badges] -->

`cmdcomp` generate command shell completion file (`bash` or `zsh`) from config
`JSON`/`YAML`/`TOML` file.

![image](./docs/images/image.png)

## Why was `cmdcomp` created?

The completion files for many cli tools (`aws`, `gcloud`, etc.) are provided by the tools themselves.
If you want to use these cli tools in multiple products or multiple environments (prd, dev, etc.),
it is useful to be able to switch contexts easily (e.g. `mycli prd aws s3 ...`).
`cmdcomp` provides a completion file for such a simple shell script wrapper.
You can easily switch between settings for each environment.

This tool can generate shell script completion files with config described in `YAML`, `TOML` or `JSON`.

Today, more and more cli tools are being used in development,
and if you want to generate a completion file for a simple wrapper script,
`cmdcomp` will be of great help.


## Install

```shell
pip install cmdcomp
```

## Usage

```shell
cmdcomp --config $YOUR_CONFIG_FILE --shell-type bash
```

## Documentation

See [documentation](https://yassun7010.github.io/cmdcomp/) for more details.

## Examples

See [examples](https://github.com/yassun7010/cmdcomp/tree/main/examples/v2).
