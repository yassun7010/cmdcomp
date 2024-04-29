#!/bin/bash
#
# Code generated by cmdcomp "$CMDCOMP_VERSION". DO NOT EDIT.
# For more information about cmdcomp, please refer to https://github.com/yassun7010/cmdcomp .
#

_cliname() {
  local word cmd opts cword cmd_cword opts_cword
  COMPREPLY=()
  cmd=""
  opts=""
  cword=0
  cmd_cword=0
  opts_cword=0

  for word in ${COMP_WORDS[@]}; do
    case "${cmd},${word}" in
      ",$1")
        cmd="_cliname"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname,list|_cliname,ls)
        cmd="_cliname_list"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname,cd)
        cmd="_cliname_cd"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname,scripts)
        cmd="_cliname_scripts"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname_scripts,run)
        cmd="_cliname_scripts_run"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname,git)
        cmd="_cliname_git"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname,gcs)
        cmd="_cliname_gcs"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname,test)
        cmd="_cliname_test"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname_test,rubocop)
        cmd="_cliname_test_rubocop"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      _cliname_test,pytest)
        cmd="_cliname_test_pytest"
        cword=$(( cword + opts_cword + 1 ))
        ;;

      *)
        opts_cword=$(( opts_cword + 1 ))
        ;;
    esac
  done

  case "${cmd}" in
    _cliname)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
        case "${COMP_WORDS[cword-1]}" in
          --verbose)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          --no-verbose)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          --version|-V)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          --config)
            if [ $cword -eq $COMP_CWORD ] ; then
              word="${COMP_WORDS[COMP_CWORD]}"
              COMPREPLY=()
              for dir in $(compgen -d -S / -- "$word"); do
                COMPREPLY+=("$dir")
              done
              for file in $(compgen -f -- "$word"); do
                [ ! -d $file ] && COMPREPLY+=("$file")
              done
              IFS=$'\n' COMPREPLY=($(sort <<<"${COMPREPLY[*]}"))
              return 0
            else
              cmd_cword=$(( cmd_cword + 2 ))
            fi
            ;;

          --type)
            if [ $cword -eq $COMP_CWORD ] ; then
              COMPREPLY=( $(compgen -W "json toml" -- "${COMP_WORDS[COMP_CWORD]}") )
              return 0
            else
              cmd_cword=$(( cmd_cword + 2 ))
            fi
            ;;

          --help)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done

      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts="--verbose --no-verbose --version -V --config --type --help"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      elif [ $cword -eq $COMP_CWORD ] ; then
        opts="list ls cd scripts git gcs test"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      return 0
      ;;

    _cliname_list)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
        case "${COMP_WORDS[cword-1]}" in
          --all|-a)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done

      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts="--all -a"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      cword=$COMP_CWORD
      if [ $cword -eq $COMP_CWORD ] ; then
        word="${COMP_WORDS[COMP_CWORD]}"
        COMPREPLY=()
        for dir in $(compgen -d -S / -- "$word"); do
          COMPREPLY+=("$dir")
        done
        for file in $(compgen -f -- "$word"); do
          [ ! -d $file ] && COMPREPLY+=("$file")
        done
        IFS=$'\n' COMPREPLY=($(sort <<<"${COMPREPLY[*]}"))
        return 0
      else
        cmd_cword=$(( cmd_cword + 2 ))
      fi
      return 0
      ;;

    _cliname_cd)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
        case "${COMP_WORDS[cword-1]}" in
          -P)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done
      if [[ ! ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        cword=$COMP_CWORD
        case $(( COMP_CWORD - cmd_cword + 1)) in
          1)
            if [ $cword -eq $COMP_CWORD ] ; then
            word="$HOME/${COMP_WORDS[COMP_CWORD]}"
            COMPREPLY=()
            for dir in $(compgen -d -S / -- "$word"); do
              COMPREPLY+=("$dir")
            done
            for file in $(compgen -f -- "$word"); do
              [ ! -d $file ] && COMPREPLY+=("$file")
            done
            IFS=$'\n' COMPREPLY=($(sort <<<"${COMPREPLY[*]#$HOME/}"))
            return 0
          else
            cmd_cword=$(( cmd_cword + 2 ))
          fi
            ;;
        esac
      fi

      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts="-P"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      return 0
      ;;

    _cliname_scripts)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
      done

      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts=""
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      elif [ $cword -eq $COMP_CWORD ] ; then
        opts="run"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      return 0
      ;;

    _cliname_scripts_run)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
        case "${COMP_WORDS[cword-1]}" in
          --all|-a)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done

      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts="--all -a"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      cword=$COMP_CWORD
      if [ $cword -eq $COMP_CWORD ] ; then
        COMPREPLY=( $(compgen -W "$(echo 'script1.sh script2.sh script3.sh')" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      else
        cmd_cword=$(( cmd_cword + 2 ))
      fi
      return 0
      ;;

    _cliname_git)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
        case "${COMP_WORDS[cword-1]}" in
          --envname)
            if [ $cword -eq $COMP_CWORD ] ; then
              COMPREPLY=( $(compgen -W "dev prd" -- "${COMP_WORDS[COMP_CWORD]}") )
              return 0
            else
              cmd_cword=$(( cmd_cword + 2 ))
            fi
            ;;

          *)
            break
            ;;
        esac
      done

      local has_keyword_splitter=false
      for word in ${COMP_WORDS[@]::$COMP_CWORD}; do
        [ "$word" == "--" ] && has_keyword_splitter=true && break
      done
      if [[ $has_keyword_splitter = false && ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts="--envname"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      local word=${COMP_WORDS[@]::$cmd_cword}
      COMP_POINT=$((COMP_POINT + 3 - ${#word} ))
      COMP_LINE="git ${COMP_WORDS[@]:$cmd_cword}"
      COMP_WORDS=($COMP_LINE)
      COMP_CWORD=$(( ${#COMP_WORDS[@]} - 1 ))
      (( COMP_CWORD < 1 )) && COMP_CWORD=1

      type "_command_offset" > /dev/null 2>&1 && _command_offset 0
      return 0
      ;;

    _cliname_gcs)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
      done

      local word=${COMP_WORDS[@]::$cmd_cword}
      COMP_POINT=$((COMP_POINT + 14 - ${#word} ))
      COMP_LINE="gcloud storage ${COMP_WORDS[@]:$cmd_cword}"
      COMP_WORDS=($COMP_LINE)
      COMP_CWORD=$(( ${#COMP_WORDS[@]} - 1 ))
      (( COMP_CWORD < 1 )) && COMP_CWORD=1

      type "_command_offset" > /dev/null 2>&1 && _command_offset 0
      return 0
      ;;

    _cliname_test)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
      done

      if [[ ${COMP_WORDS[COMP_CWORD]} == -* ]] ; then
        opts=""
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      elif [ $cword -eq $COMP_CWORD ] ; then
        opts="rubocop pytest"
        COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
        return 0
      fi
      return 0
      ;;

    _cliname_test_rubocop)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
        case "${COMP_WORDS[cword-1]}" in
          --auto-correct|-A)
            cmd_cword=$(( cmd_cword + 1 ))
            ;;

          *)
            break
            ;;
        esac
      done

      opts="--auto-correct -A"
      COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
      return 0
      ;;

    _cliname_test_pytest)
      cmd_cword=$cword
      while [ $cword -lt $COMP_CWORD ] ; do
        cword=$(( cword + 1 ))
      done

      opts=""
      COMPREPLY=( $(compgen -W "${opts}" -- "${COMP_WORDS[COMP_CWORD]}") )
      return 0
      ;;

  esac
}

complete -F _cliname -o bashdefault cliname
complete -F _cliname -o bashdefault cliname2
