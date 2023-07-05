#!/bin/zsh

_() {
    shift words

    case "$(($CURRENT-1))" in
        1)
            _values '' welcome list ls execute restart shell log cd test and_normal_options_work ;;
        2)
            case ${words[1]} in
                execute|restart|shell|log)
                    _values 'execute|restart|shell|log' $(your_app_name ps -s) ;;
                cd)
                    _files -W "$(cd $(dirname $0); pwd)/../apps" ;;
                test)
                    _values 'test' rubocop ;;
                and_normal_options_work)
                    _values 'and_normal_options_work' foo bar ;;
            esac ;;
    esac
}

compdef _ 
