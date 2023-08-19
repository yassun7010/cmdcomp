# Argument

This item sets the completion candidates for each command argument.

## Select Argument

If you want to choise several candidates, use `select` type argument.

=== "yaml"

    ```yaml
    cmdcomp:
      version: "2"
    app:
      name: mycli
    root:
      arguments:
        --format:
          type: select
          description: output format.
          values:
            - json
            - yaml
            - toml
    ```

=== "toml"

    ```toml
    [cmdcomp]
    version = "2"

    [app]
    name = "mycli"

    [root.arguments.--format]
    type = "select"
    description = "output format."
    values = ["json", "yaml", "toml"]
    ```

## File Argument

If you want the output to be a candidate for file path completion, the `file`
type is recommended.

=== "yaml"

    ```yaml
    cmdcomp:
      version: "2"
    app:
      name: mycli
    root:
      arguments:
        --output:
          type: file
          description: output filename.
    ```

=== "toml"

    ```toml
    [cmdcomp]
    version = "2"

    [app]
    name = "mycli"

    [root.arguments.--output]
    type = "file"
    description = "output filename."
    ```

By default, it outputs completion candidates starting from the current directory
of the shell, but you can change the starting directory by specifying
`base_path`.

=== "yaml"

    ```yaml
    cmdcomp:
      version: "2"
    app:
      name: mycli
    root:
      arguments:
        --list:
          type: file
          description: list my command targets.
          base_path: $HOME/.mycmd/targets
    ```

=== "toml"

    ```toml
    [cmdcomp]
      version = "2"

    [app]
    name = "mycli"

    [root.arguments.--list]
    type = "file"
    description = "list my command targets."
    base_path = "$HOME/.mycmd/targets"
    ```

For more complex conditions, such as outputting only files with a specific file
extension, consider using the [command](#command-argument) type.

## Command Argument

If you want to make the result of executing any command a completion candidate,
use the `command` type.

=== "yaml"

    ```yaml
    cmdcomp:
      version: "2"
    app:
      name: mycli
    root:
      arguments:
        --start-date:
          type: command
          description: start date.
          execute: date +%Y-%m-%d
    ```

=== "toml"

    ```toml
    [cmdcomp]
    version = "2"

    [app]
    name = "mycli"

    [root.arguments.--start-date]
    type = "command"
    description = "start date."
    execute = "date +%Y-%m-%d"
    ```
