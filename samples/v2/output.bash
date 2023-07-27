#!/bin/bash

_cliname() {
  local i cur prev opts cmd
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"
  cmd=""
  opts=""

  for i in ${COMP_WORDS[@]} do
    case "${cmd},${i}" in
      ",$1")
        cmd="cliname"
        ;;

      cliname,list)
        cmd="_cliname_list_subcommands"
        ;;

      cliname,cd)
        cmd="_cliname_cd_subcommands"
        ;;

      cliname,test)
        cmd="_cliname_test_subcommands"
        ;;

      *)
        ;;
    esac
  done
}

complete -F _cliname -o bashdefault -o default cliname
