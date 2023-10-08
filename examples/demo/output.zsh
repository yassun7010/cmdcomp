#!/bin/zsh
#
# Code generated by cmdcomp "$CMDCOMP_VERSION". DO NOT EDIT.
# For more information about cmdcomp, please refer to https://github.com/yassun7010/cmdcomp .
#

_mycli() {
  local context curcontext=$curcontext state line
  declare -A opt_args
  local ret=1
  local cmd_name=mycli

  case $cmd_name in
    mycli)
      local -a __mycli_subcmds
      __mycli_subcmds=(
        gcloud'[gcloud command.]'
        gcs'[gcs command.]'
        composer-operation'[composer operation command.]'
        git'[git command.]'
        test'[test command.]'
      )

      _arguments -C \
        --verbose'[verbose output.]' \
        --help'[print help.]' \
        '1: :_values "subcommand" ${__mycli_subcmds[@]}' \
        '*:: :->args' \
        && ret=0

      cmd_name=$words[1]
      case $state in
        args)
          case $cmd_name in
            gcloud)
              words=(gcloud "${words[2, -1]}")
              ((CURRENT += 0))
              _normal
              ;;

            gcs)
              words=(gcloud storage "${words[2, -1]}")
              ((CURRENT += 1))
              _normal
              ;;

            composer-operation)
              words=(gcloud composer operations "${words[2, -1]}")
              ((CURRENT += 2))
              _normal
              ;;

            git)
              words=(git "${words[2, -1]}")
              ((CURRENT += 0))
              _normal
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

compdef _mycli mycli
