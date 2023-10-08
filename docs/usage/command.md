# Command

This item sets the completion candidates for each command.

The complete configuration items are as follows.

The overall structure of the [Command](#command) is shown below.

=== "Use positional arguments"

    ```yaml
    --8<-- "docs/data/jinja/v2_positional_arguments_command_structure.yaml.jinja"
    ```

    | Property    | Required | Type                        | Description          |
    | ----------- | -------- | --------------------------- | -------------------- |
    | description |          | `str | None`                | command description. |
    | alias       |          | `str | list[str] | None`    | command alias.       |
    | arguments   |          | `dict[str | int, Argument]` | command arguments.   |

    The following 3 types of `arguments` keys are available.

    | Examples               | Description                                                                                          |
    | ---------------------- | ---------------------------------------------------------------------------------------------------- |
    | `1`, `2`               | Positional argument.                                                                                 |
    | `"--help"`, <br>`"-v"` | Keyword argument.                                                                                    |
    | `"*"`                  | Wildcard argument (The same rule applies to all positions not specified in the positional argument). |

=== "Use subcommands"

    ```yaml
    --8<-- "docs/data/jinja/v2_subcommands_command_structure.yaml.jinja"
    ```

    | Property    | Required | Type                        | Description          |
    | ----------- | -------- | --------------------------- | -------------------- |
    | description |          | `str | None`                | command description. |
    | alias       |          | `str | list[str] | None`    | command alias.       |
    | arguments   |          | `dict[str | int, Argument]` | command arguments.   |
    | subcommands |          | `dict[str, Command]`        | Subcommands.         |

    The following 3 types of `arguments` keys are available.

    | Examples           | Description                                                                                          |
    | ------------------ | ---------------------------------------------------------------------------------------------------- |
    | `"--help"`, `"-v"` | Keyword argument.                                                                                    |

=== "Use delegate"

    ```yaml
    --8<-- "docs/data/jinja/v2_delegate_command_structure.yaml.jinja"
    ```

    | Property    | Required | Type                        | Description          |
    | ----------- | -------- | --------------------------- | -------------------- |
    | type        | ✅        | `Literal["delegate"]`       | command type.        |
    | description |          | `str | None`                | command description. |
    | alias       |          | `str | list[str] | None`    | command alias.       |
    | target      | ✅        | `str | list[str]`           | delegate target.     |
