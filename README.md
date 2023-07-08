# Command Completion Generator Tool

`cmdcomp` generate shell completion file (bash or zsh) from config toml file.

## Usage

```shell
docker run --rm -itv $(pwd):/apps/cmdcomp yassun4dev/cmdcomp --file ${YOUR_LOCAL_TOML_FILE} --shell-type bash
```
