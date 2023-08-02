#!/bin/zsh
#
# Code generated by cmdcomp "2.0.3". DO NOT EDIT.
# For more information about cmdcomp, please refer to https://github.com/yassun4dev/cmdcomp .
#

_your_cli_command_name() {
    shift words

    case "$(($CURRENT-1))" in
        1)
            _values 'your_cli_command_name' -h --help --version welcome list ls execute restart shell log cd test and-normal-options-work
            ;;
        2)
            case ${words[1]} in
                list|ls)
                    _values 'list|ls' -a
                    ;;
                execute|restart|shell|log)
                    _values 'execute|restart|shell|log' $(your_app_name ps -s)
                    ;;
                cd)
                    _files -W "$(cd $(dirname $0); pwd)/../apps"
                    ;;
                test)
                    _values 'test' rubocop
                    ;;
                and-normal-options-work)
                    _values 'and_normal_options_work' -h --help foo bar
                    ;;
            esac
            ;;
        3)
            case ${words[1]} in
                test)
                    case ${words[2]} in
                        rubocop)
                            _values 'rubocop' -A
                            ;;
                    esac
                    ;;
            esac
            ;;
    esac
}

compdef _your_cli_command_name your_cli_command_name
compdef _your_cli_command_name cli_alias_name
