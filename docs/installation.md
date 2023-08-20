# Installation

## PyPi

Instration is as simple as:

```sh
pip install cmdcomp
```

!!! success "Recommendation"

    You can also use pipx to install `cmdcomp` in a application dedicated virtual
    environment created for you.

    ```sh
    pipx install cmdcomp
    ```

## Docker

To run on Docker, you can do the following

```shell
docker run --rm -itv $(pwd):/app/cmdcomp yassun7010/cmdcomp --file ${YOUR_CONFIG_FILE} --shell-type bash
```
