#!/bin/bash

_cliname() {
  local word cur cmd cmd_cur opts
  COMPREPLY=()
  cur=0
  cmd_cur=0
  cmd=""
  opts=""

  for word in ${COMP_WORDS[@]}; do
    case "${cmd},${word}" in
      ",$1")
        cmd="_cliname"
        cur=$(( cur + 1 ))
        ;;

      _cliname,list|_cliname,ls)
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
      opts="list ls cd test --verbose --no-verbose --version -V --config --help"
      if [[ ${COMP_CWORD} -eq 1 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      cmd_cur=$cur
      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))
        case "${COMP_WORDS[cur-1]}" in
          --verbose)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          --no-verbose)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          --version|-V)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          --config)
            if [ $cur -eq $COMP_CWORD ] ; then
              file_completion "."

              return 0
            else
              cmd_cur=$(( cmd_cur + 2 ))
            fi
            ;;

          --help)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done

      return 0
      ;;

    _cliname_list)
      opts="--all -a"
      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      cmd_cur=$cur
      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))
        case "${COMP_WORDS[cur-1]}" in
          --all|-a)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done
      cur=$COMP_CWORD
      case $(( COMP_CWORD - cmd_cur + 1)) in
        *)
          cur=$COMP_CWORD
          if [ $cur -eq $COMP_CWORD ] ; then
            file_completion "."

            return 0
          else
            cmd_cur=$(( cmd_cur + 2 ))
          fi
          ;;
      esac

      return 0
      ;;

    _cliname_cd)
      opts="-P"
      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      cmd_cur=$cur
      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))
        case "${COMP_WORDS[cur-1]}" in
          -P)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done
      cur=$COMP_CWORD
      case $(( COMP_CWORD - cmd_cur + 1)) in
        1)
          if [ $cur -eq $COMP_CWORD ] ; then
            file_completion "$HOME"

            return 0
          else
            cmd_cur=$(( cmd_cur + 2 ))
          fi
          ;;
      esac

      return 0
      ;;

    _cliname_test)
      opts="rubocop pytest"
      if [[ ${COMP_CWORD} -eq 2 ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      cmd_cur=$cur
      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))
      done

      return 0
      ;;

    _cliname_test_rubocop)
      opts="--auto-correct -A"
      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      cmd_cur=$cur
      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))
        case "${COMP_WORDS[cur-1]}" in
          --auto-correct|-A)
            cmd_cur=$(( cmd_cur + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done

      return 0
      ;;

    _cliname_test_pytest)
      opts=""
      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[cur]}") )
        return 0
      fi

      cmd_cur=$cur
      while [ $cur -lt $COMP_CWORD ] ; do
        cur=$(( cur + 1 ))
      done

      return 0
      ;;

  esac
}

complete -F _cliname -o bashdefault -o default cliname
