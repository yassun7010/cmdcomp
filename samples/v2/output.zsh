#!/bin/zsh

_cliname() {
    local context curcontext=$curcontext state line
    declare -A opt_args
    local ret=1
    local -a _subcmds
    _subcmds=(
        'sub1[sub1 description]'
        'sub2[sub2 description]'
    )

    _arguments -C \
        {--file,-f}'[config filepath.]:file:_files -W "$HOME"' \
        {--output,-o}'[output filename.]:file:_files' \
        --shell'[shell name.]:values:(bash zsh)' \
        --ls'[ls command]:command:_values 'ls' $(ls | grep -e '\.md$')' \
        --verbose'[verbose description]' \
        --no-verbose'[no verbose description]' \
        --help'' \
        1': :_values "subcommand" ${_subcmds[@]}' \
        '*:: :->args' \
        && ret=0

    case $state in
        (args)
            case $words[1] in
                (sub1)
                    _arguments '-s[sort output]' '--l[long output]' '-l[long output]' && ret=0
                    ;;
                (sub2)
                    _arguments '-s[sort output]' '--l[long output]' '-l[long output]' && ret=0
                    ;;
            esac
            ;;
    esac

    return ret
}

compdef _cliname cliname cliname2
