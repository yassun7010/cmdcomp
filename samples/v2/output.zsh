#!/bin/zsh

_cliname() {
    local context curcontext=$curcontext state line
    declare -A opt_args
    local ret=1

    _arguments -C \
        '--file[config filepath.]' \
        '--verbose[verbose description]' \
        '--no-verbose' \
        '*:: :->null' \
        && return 1

    return 0
}

compdef _cliname cliname cliname2
