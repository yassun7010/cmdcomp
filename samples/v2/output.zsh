#!/bin/zsh

_cliname() {
  local context curcontext=$curcontext state line
  declare -A opt_args
  local ret=1
  local cmd_name=cliname

  case $cmd_name in
    cliname)
      local -a __cliname_subcmds
      __cliname_subcmds=(
        {list,ls}'[list project files.]'
        cd'[cd project directory.]'
        test'[test command.]'
      )

      _arguments -C \
        --verbose'[verbose output.]' \
        --no-verbose'[no verbose output.]' \
        {--version,-V}'[print version.]' \
        --config'[config file.]:file:_files' \
        --help'[print help.]' \
        '1: :_values "subcommand" ${__cliname_subcmds[@]}' \
        '*:: :->args' \
        && ret=0

      cmd_name=$words[1]
      case $state in
        args)
          case $cmd_name in
            list|ls)
              _arguments -C \
                {--all,-a}'[list all files.]' \
                '*:file:_files' \
                && ret=0
              ;;

            cd)
              _arguments -C \
                -P'[physical directory.]' \
                '1:file:_files -W "$HOME"' \
                && ret=0
              ;;

            test)
              local -a __test_subcmds
              __test_subcmds=(
                rubocop'[run rubocop.]'
                pytest'[run pytest.]'
              )

              _arguments -C \
                '1: :_values "subcommand" ${__test_subcmds[@]}' \
                '*:: :->args' \
                && ret=0

              cmd_name=$words[1]
              case $state in
                args)
                  case $cmd_name in
                    rubocop)
                      _arguments -C \
                        {--auto-correct,-A}'[auto correct.]' \
                        && ret=0
                      ;;

                    pytest)
                      _arguments -C \
                        && ret=0
                      ;;

                  esac
                  ;;

              esac
              ;;

          esac
          ;;

      esac
      ;;

  esac

  return ret
}

compdef _cliname cliname cliname2
