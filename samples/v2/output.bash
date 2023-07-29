#!/bin/bash

_cliname() {
  local word cur prev cmd opts
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"
  cmd=""
  opts=""

  for word in ${COMP_WORDS[@]}; do
    case "${cmd},${word}" in
      ",$1")
        cmd="_cliname"
        ;;

      _cliname,list)
        cmd="_cliname_list"
        ;;

      _cliname,cd)
        cmd="_cliname_cd"
        ;;

      _cliname,test)
        cmd="_cliname_test"
        ;;

      _cliname_test,rubocop)
        cmd="_cliname_test_rubocop"
        ;;

      _cliname_test,pytest)
        cmd="_cliname_test_pytest"
        ;;

      *)
        ;;
    esac
  done

  case "${cmd}" in
    _cliname)
      opts="list cd test --verbose --no-verbose --version --config --help"
      if [[ ${cur} == -* || ${COMP_CWORD} -eq 1 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
      fi

      case "${prev}" in
        --verbose)
          COMPREPLY=()
          ;;

        --no-verbose)
          COMPREPLY=()
          ;;

        --version)
          COMPREPLY=()
          ;;

        --config)
          file_completion "."
          ;;

        --help)
          COMPREPLY=()
          ;;

        *)
          COMPREPLY=()
          ;;

      esac

      return 0
      ;;

    _cliname_list)
      opts="--all"
      if [[ ${cur} == -* || ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
      fi

      case "${prev}" in
        --all)
          COMPREPLY=()
          ;;

        *)
          file_completion "."
          ;;

      esac

      return 0
      ;;

    _cliname_cd)
      opts=""
      if [[ ${cur} == -* || ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
      fi

      case "${prev}" in
        *)
          file_completion "."
          ;;
        

      esac

      return 0
      ;;

    _cliname_test)
      opts="rubocop pytest"
      if [[ ${cur} == -* || ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
      fi

      case "${prev}" in
        *)
          COMPREPLY=()
          ;;

      esac

      return 0
      ;;

    _cliname_test_rubocop)
      opts="--auto-correct"
      if [[ ${cur} == -* || ${COMP_CWORD} -eq 3 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
      fi

      case "${prev}" in
        --auto-correct)
          COMPREPLY=()
          ;;

        *)
          COMPREPLY=()
          ;;

      esac

      return 0
      ;;

    _cliname_test_pytest)
      opts=""
      if [[ ${cur} == -* || ${COMP_CWORD} -eq 3 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
        return 0
      fi

      case "${prev}" in
        *)
          COMPREPLY=()
          ;;

      esac

      return 0
      ;;

  esac
}

complete -F _cliname -o bashdefault -o default cliname
