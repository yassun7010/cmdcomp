#!/usr/bin/env bats

log_filename=_test.log
result_filename=_result.log
expected_filename=_expected.log

output_state() {
    echo COMP_LINE=${COMP_LINE}
    echo COMP_POINT=${COMP_POINT}
    echo COMP_WORDS=${COMP_WORDS[@]}
    echo COMP_CWORD=${COMP_CWORD}
    echo COMPREPLY=${COMPREPLY[@]}
    echo
}

output_list() {
    shopt -s extglob
    array=("$@")
    array=("${array[@]/#+([[:blank:]])/}")
    array=("${array[@]/%+([[:blank:]])/}")

    IFS=$'\n' sorted=$(sort <<<${array[*]})
    unset IFS
    printf "%s\n" "${sorted[@]}"
}

calc_completion() {
    source examples/v2/output.bash
    COMPREPLY=()
    COMP_WORDBREAKS="
\"'><=;|&(:"
    COMP_LINE="$@"
    COMP_WORDS=("$@")
    COMP_POINT=${COMP_POINT:-${#COMP_LINE}}
    COMP_CWORD=${COMP_CWORD:-${#COMP_WORDS[@]}}

    echo Before: >$log_filename
    output_state >>$log_filename

    ${COMP_COMMAND:-_cliname} "$1"
}

assert_eq() {
    result=$(output_list "${COMPREPLY[@]}")
    expected=$(output_list "$@")

    echo "$result" >$result_filename
    echo "$expected" >$expected_filename

    git diff --no-index --color=always "$expected_filename" "$result_filename" || {
        echo After: >>$log_filename
        output_state >>$log_filename
        return 1
    }
}

@test "completion command only" {
    calc_completion cliname

    assert_eq list ls cd scripts git test
}

@test "completion command alias" {
    calc_completion cliname2

    assert_eq list ls cd scripts git test
}

@test "completion command flag option" {
    calc_completion cliname --verbose

    assert_eq list ls cd scripts git test
}

@test "completion command file option" {
    calc_completion cliname --config

    assert_eq $(ls -Ap | sort | cat)
}

@test "completion command select option" {
    calc_completion cliname --type

    assert_eq json toml
}

@test "completion subcommand" {
    calc_completion cliname list

    assert_eq $(ls -Ap | sort | cat)
}

@test "completion subcommand with flag" {
    COMP_CWORD=2 calc_completion cliname list --

    assert_eq --all
}

@test "completion subcommand with kwarg" {
    COMP_CWORD=2 calc_completion cliname --config examples/v2/config.cmdcomp.

    assert_eq examples/v2/config.cmdcomp.toml examples/v2/config.cmdcomp.yaml
}

@test "completion file arg with base_path" {
    COMP_CWORD=2 calc_completion cliname cd

    assert_eq "$(ls -Ap $HOME | sed 's/bash_completion.d/bash_completion.d\//g')"
}

@test "completion subsubcommand" {
    calc_completion cliname test

    assert_eq rubocop pytest
}

@test "completion git" {
    source ~/.bash_completion.d/git-completion.bash
    COMP_COMMAND=__git_wrap__git_main calc_completion git

    assert_eq add am archive bisect branch bundle checkout cherry-pick citool clean clone commit describe diff fetch format-patch gc grep gui init log maintenance merge mv notes pull push range-diff rebase reset restore revert rm shortlog show sparse-checkout stash status submodule switch tag worktree gitk scalar credential-gcloud credential-gcloud.sh lfs open apply blame cherry config difftool fsck help instaweb mergetool prune reflog remote repack replace request-pull send-email show-branch stage whatchanged
}

# bash_completion を利用するとエラーになる。
#
# @test "completion delegate" {
#     source /opt/homebrew/share/bash-completion/bash_completion
#     source ~/.bash_completion.d/git-completion.bash
#     calc_completion cliname git a

#     assert_eq add am archive bisect branch bundle checkout cherry-pick citool clean clone commit describe diff fetch format-patch gc grep gui init log maintenance merge mv notes pull push range-diff rebase reset restore revert rm shortlog show sparse-checkout stash status submodule switch tag worktree gitk scalar credential-gcloud credential-gcloud.sh lfs open apply blame cherry config difftool fsck help instaweb mergetool prune reflog remote repack replace request-pull send-email show-branch stage whatchanged
# }
