#!/usr/bin/env bats

log_filename=test.log

output_state() {
    echo COMP_LINE=${COMP_LINE}
    echo COMP_POINT=${COMP_POINT}
    echo COMP_WORDS=${COMP_WORDS[@]}
    echo COMP_CWORD=${COMP_CWORD}
    echo COMPREPLY=${COMPREPLY[@]}
    echo
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

    _cliname "$1"
}

assert_eq() {
    local result=${COMPREPLY[@]}
    local expected="$@"

    echo "Result: $result" >>$log_filename
    echo >>$log_filename
    echo "Expected: $expected" >>$log_filename
    echo >>$log_filename

    [[ "$result" == "$expected" ]] && {
        echo Success >>$log_filename
        return 0
    } || {
        echo Error: >>$log_filename
        output_state >>$log_filename
        return 1
    }
}

@test "completion command only" {
    calc_completion cliname

    assert_eq "list ls cd scripts gcloud test"
}

@test "completion command alias" {
    calc_completion cliname2

    assert_eq "list ls cd scripts gcloud test"
}

@test "completion command flag option" {
    calc_completion cliname --verbose

    assert_eq "list ls cd scripts gcloud test"
}

@test "completion command file option" {
    calc_completion cliname --config

    assert_eq $(ls -Ap | cat)
}

@test "completion command select option" {
    calc_completion cliname --type

    assert_eq json toml
}

@test "completion subcommand" {
    calc_completion cliname list

    assert_eq $(ls -Ap | cat)
}

@test "completion subcommand with kwarg" {
    COMP_CWORD=2 calc_completion cliname --config examples/v2/config.cmdcomp.

    assert_eq examples/v2/config.cmdcomp.toml examples/v2/config.cmdcomp.yaml
}
