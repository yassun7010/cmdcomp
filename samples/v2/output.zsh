#!/bin/zsh

function _cliname () {
    local context curcontext=$curcontext state line
    declare -A opt_args
    local ret=1

    _arguments -C \
        {-f,--file}'[config filepath.]:filename:_files' \
        '--verbase[verbose description]' \
        '--no-verbose' \
        '*:: :->null' \
        && ret=0

    return ret
}

compdef _cliname cliname
