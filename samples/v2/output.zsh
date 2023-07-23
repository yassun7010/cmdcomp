#!/bin/zsh

_cliname() {
    local context curcontext=$curcontext state line
    declare -A opt_args
    local ret=1

    _arguments -C \
        {--file,-f}'[config filepath.]:file:_files -W "$HOME"' \
        {--output,-o}'[output filename.]:file:_files' \
        --shell'[shell name.]:values:(bash zsh)' \
        --ls'[ls command]:command:_values 'ls' $(ls | grep -e '\.md$')' \
        --verbose'[verbose description]' \
        --no-verbose'[no verbose description]' \
        --help'' \
        '*:: :->null' \
        && return 1

    return 0
}

compdef _cliname cliname cliname2
