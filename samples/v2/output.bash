#!/bin/bash

_cliname() {
  local i cur prev opts cmd
  COMPREPLY=()
  cur="${COMP_WORDS[COMP_CWORD]}"
  prev="${COMP_WORDS[COMP_CWORD-1]}"
  cmd=""
  opts=""

  for i in ${COMP_WORDS[@]}; do
    case "${cmd},${i}" in
      ",$1")
        cmd="_cliname"
        ;;

      _cliname_subcommand,list)
        cmd="_cliname_list_subcommand"
        ;;

      _cliname_subcommand,cd)
        cmd="_cliname_cd_subcommand"
        ;;

      _cliname_subcommand,test)
        cmd="_cliname_test_subcommand"
        ;;

      _cliname_test_subcommand,rubocop)
        cmd="_cliname_test_rubocop_subcommand"
        ;;

      _cliname_test_subcommand,pytest)
        cmd="_cliname_test_pytest_subcommand"
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

    _cliname_list_subcommand)
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
              COMPREPLY=()
              ;;

      esac

      return 0
      ;;

    _cliname_cd_subcommand)
      opts=""
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

    _cliname_test_subcommand)
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

    _cliname_test_rubocop_subcommand)
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

    _cliname_test_pytest_subcommand)
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
