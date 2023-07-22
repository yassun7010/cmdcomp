#!/bin/zsh

_cliname() {
    local context curcontext=$curcontext state line
    declare -A opt_args
    local ret=1

    _arguments -C \
        '--file[config filepath.]:file:_files' \
        '--verbose[verbose description]' \
        '--no-verbose' \
        '1: arg:(arg1)' \
        '2: arg:(arg1 arg2 arg3)' \
        '3: arg:(arg1 arg2)' \
        '*:: :->null' \
        && return 1

    return 0
}

compdef _cliname cliname cliname2
