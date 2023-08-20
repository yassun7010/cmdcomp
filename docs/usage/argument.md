# Argument

This item sets the completion candidates for each command argument.

## Select Argument

If you want to choise several candidates, use `select` type argument.

=== "yaml"

    ```yaml
    --8<-- "config/config_v2_select_argument.yaml"
    ```

=== "toml"

    ```toml
    --8<-- "config/config_v2_select_argument.toml"
    ```

## File Argument

If you want the output to be a candidate for file path completion, the `file`
type is recommended.

=== "yaml"

    ```yaml
    --8<-- "config/config_v2_file_argument.yaml"
    ```

=== "toml"

    ```toml
    --8<-- "config/config_v2_file_argument.toml"
    ```

By default, it outputs completion candidates starting from the current directory
of the shell, but you can change the starting directory by specifying
`base_path`.

=== "yaml"

    ```yaml
    --8<-- "config/config_v2_file_argument_with_base_path.yaml"
    ```

=== "toml"

    ```toml
    --8<-- "config/config_v2_file_argument_with_base_path.toml"
    ```

For more complex conditions, such as outputting only files with a specific file
extension, consider using the [command](#command-argument) type.

## Command Argument

If you want to make the result of executing any command a completion candidate,
use the `command` type.

=== "yaml"

    ```yaml
    --8<-- "config/config_v2_command_argument.yaml"
    ```

=== "toml"

    ```toml
    --8<-- "config/config_v2_command_argument.toml"
    ```
