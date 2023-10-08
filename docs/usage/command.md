# Command

This item sets the completion candidates for each command.

The complete configuration items are as follows.

The overall structure of the [Command](#command) is shown below.

=== "Use positional arguments"

    ```yaml
    --8<-- "docs/data/jinja/v2_positional_arguments_command_structure.yaml.jinja"
    ```

=== "Use subcommands"

    ```yaml
    --8<-- "docs/data/jinja/v2_subcommands_command_structure.yaml.jinja"
    ```

| Property    | Type                              | Description          |
| ----------- | --------------------------------- | -------------------- |
| description | `str | None`                      | Command description. |
| alias       | `str | list[str] | None`          | Command alias.       |
| arguments   | `dict[str | int, Argument]`       | Arguments.           |
| subcommands | `dict[str, Command]`              | Subcommands.         |

The following 3 types of `arguments` keys are available.

| Examples           | Description                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| `1`, `2`           | Positional argument.                                                                                  |
| `"--help"`, `"-v"` | Keyword argument.                                                                                     |
| `"*"`              | Wildcard argument (The same rule applies to all positions not specified in the positional argument). |

!!! warning

    When `subcommands` are used, the keys of the `arguments` can use only keyword argument key.
