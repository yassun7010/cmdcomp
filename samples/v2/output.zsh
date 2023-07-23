#!/bin/zsh

_cliname() {
    local context curcontext=$curcontext state line
    declare -A opt_args
    local ret=1

    _arguments -C \
        '1: arg:(arg1)' \
        '2: arg:(arg2 arg21)' \
        '3: arg:(arg3 arg31 arg32)' \
        '*: arg:(arg4 arg41 arg42 arg43)' \
        && return 1

    return 0
}

compdef _cliname cliname cliname2
