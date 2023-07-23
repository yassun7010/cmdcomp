#!/bin/zsh

_cliname() {
  local context curcontext=$curcontext state line
  declare -A opt_args
  local ret=1
  local cmd_name=cliname

  case $cmd_name in
    (cliname)
      local -a __cliname_subcmds
      __cliname_subcmds=(
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
        1': :_values "subcommand" ${__cliname_subcmds[@]}' \
        '*:: :->args' \
        && ret=0

      cmd_name=$words[1]
      case $state in
        (args)
          case $cmd_name in
            (sub1)

              _arguments -C \
                {--file,-f}'[config filepath.]:file:_files -W "$HOME"' \
                '1: arg:(arg1)' \
                '2: arg:(arg2 arg21)' \
                '3: arg:(arg3 arg31 arg32)' \
                '*: arg:(arg4 arg41 arg42 arg43)' \
                && ret=0

              ;;
            (sub2)

              _arguments -C \
                --verbose'[verbose description]' \
                --no-verbose'[no verbose description]' \
                && ret=0

              ;;
          esac
          ;;
      esac
      ;;
  esac

  return ret
}

compdef _cliname cliname cliname2
