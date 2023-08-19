# Installation

## PyPi　(Recommendation)

Instration is as simple as:

```sh
pip install cmdcomp
```

!!! success

    You can also use pipx to install `cmdcomp` in a application dedicated virtual
    environment created for you.

    ```sh
    pipx install cmdcomp
    ```

## Docker

Docker support is available for those who wish to use it and run it in a
container.

```shell
docker run --rm -itv $(pwd):/app/cmdcomp yassun7010/cmdcomp --file ${YOUR_CONFIG_FILE} --shell-type bash
```
