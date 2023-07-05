#!/bin/bash

_() {
    local cur prev words cword split
    _init_completion || return

    case $cword in
        1)
            COMPREPLY=( $(compgen -W "welcome list ls execute restart shell log cd test and_normal_options_work" -- "$cur") ) ;;
        2)
            case ${words[1]} in
                execute|restart|shell|log)
                    COMPREPLY=( $(compgen -W "$(your_app_name ps -s)" -- "$cur") ) ;;
                cd)
                    file_completion "$(cd $(dirname $0); pwd)/../apps" ;;
                test)
                    COMPREPLY=( $(compgen -W "rubocop" -- "$cur") ) ;;
                and_normal_options_work)
                    COMPREPLY=( $(compgen -W "foo bar" -- "$cur") ) ;;
            esac ;;
    esac
}

file_completion() {
    local cur prev cword opts
    _get_comp_words_by_ref -n : cur prev cword
    dir="$(echo ${cur} | grep -o ".*/")"
    if test "${dir}" ;then
        COMPREPLY=( $(compgen -W "$(ls -F $1/${dir} | sed -E "s@(.*)@${dir}\1@g")" -- "${cur}") )
    else
        COMPREPLY=( $(compgen -W "$(ls -F $1/)" -- "${cur}") )
    fi
}

complete -F _ 
