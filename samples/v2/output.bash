#!/bin/bash

_cliname() {
  local word cur cmd opts
  COMPREPLY=()
  cur=0
  cmd=""
  opts=""

  for word in ${COMP_WORDS[@]}; do
    case "${cmd},${word}" in
      ",$1")
        cmd="_cliname"
        cur=$(( cur + 1 ))
        ;;

      _cliname,list)
        cmd="_cliname_list"
        cur=$(( cur + 1 ))
        ;;

      _cliname,cd)
        cmd="_cliname_cd"
        cur=$(( cur + 1 ))
        ;;

      _cliname,test)
        cmd="_cliname_test"
        cur=$(( cur + 1 ))
        ;;

      _cliname_test,rubocop)
        cmd="_cliname_test_rubocop"
        cur=$(( cur + 1 ))
        ;;

      _cliname_test,pytest)
        cmd="_cliname_test_pytest"
        cur=$(( cur + 1 ))
        ;;

      *)
        ;;
    esac
  done

  case "${cmd}" in
    _cliname)
      opts="list cd test --verbose --no-verbose --version --config --help"
      if [[ ${COMP_CWORD} -eq 1 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))

        case "${COMP_WORDS[cur-1]}" in
          --verbose)
            if [ $cur -eq $COMP_CWORD ] ; then
              COMPREPLY=()
              return 0
            fi
            
            ;;

          --no-verbose)
            if [ $cur -eq $COMP_CWORD ] ; then
              COMPREPLY=()
              return 0
            fi
            
            ;;

          --version)
            if [ $cur -eq $COMP_CWORD ] ; then
              COMPREPLY=()
              return 0
            fi
            
            ;;

          --config)
            if [ $cur -eq $COMP_CWORD ] ; then
              file_completion "."
              return 0
            fi
            
            ;;

          --help)
            if [ $cur -eq $COMP_CWORD ] ; then
              COMPREPLY=()
              return 0
            fi
            
            ;;

          *)
            COMPREPLY=()
            ;;

        esac
      done

      return 0
      ;;

    _cliname_list)
      opts="--all"
      if [[ ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))

        case "${COMP_WORDS[cur-1]}" in
          --all)
            if [ $cur -eq $COMP_CWORD ] ; then
              COMPREPLY=()
              return 0
            fi
            
            ;;

          *)
          if [ $cur -eq $COMP_CWORD ] ; then
            file_completion "."
            return 0
          fi
          ;;

        esac
      done

      return 0
      ;;

    _cliname_cd)
      opts=""
      if [[ ${cur} == -* && ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))

        case "${COMP_WORDS[cur-1]}" in
          *)
          if [ $cur -eq $COMP_CWORD ] ; then
            file_completion "$HOME"
            return 0
          fi
          ;;

        esac
      done

      return 0
      ;;

    _cliname_test)
      opts="rubocop pytest"
      if [[ ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))

        case "${COMP_WORDS[cur-1]}" in
          *)
            COMPREPLY=()
            ;;

        esac
      done

      return 0
      ;;

    _cliname_test_rubocop)
      opts="--auto-correct"
      if [[ ${COMP_CWORD} -eq 3 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))

        case "${COMP_WORDS[cur-1]}" in
          --auto-correct)
            if [ $cur -eq $COMP_CWORD ] ; then
              COMPREPLY=()
              return 0
            fi
            
            ;;

          *)
            COMPREPLY=()
            ;;

        esac
      done

      return 0
      ;;

    _cliname_test_pytest)
      opts=""
      if [[ ${COMP_CWORD} -eq 3 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))

        case "${COMP_WORDS[cur-1]}" in
          *)
            COMPREPLY=()
            ;;

        esac
      done

      return 0
      ;;

  esac
}

complete -F _cliname -o bashdefault -o default cliname
