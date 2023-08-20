# Command

This item sets the completion candidates for each command.

The complete configuration items are as follows.

The overall structure of the [Command](#command) is shown below.

```yaml
description: command description.
alias: my-cmd
arguments:
  1:
    {{ Argument }}
  --help:
    {{ Argument }}
  *:
    {{ Argument }}
subcommands:
  list:
    {{ Command }}
  run:
    {{ Command }}
```

| Property    | Type                              | Description          |
| ----------- | --------------------------------- | -------------------- |
| description | `str`                             | Command description. |
| alias       | `Union[str, list[str]]`           | Command alias.       |
| arguments   | `Dict[Union[str, int], Argument]` | Arguments.           |
| subcommands | `Dict[str, Command]`              | Subcommands.         |

The following 3 types of `arguments` keys are available.

| Examples           | Description                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| `1`, `2`           | Positional argument.                                                                                  |
| `"--help"`, `"-v"` | Keyword argument.                                                                                     |
| `"*"`              | Whildcard argument (The same rule applies to all positions not specified in the positional argument). |

!!! warning

    When `subcommands` are used, the keys of the `arguments` can use only keyword argument key.