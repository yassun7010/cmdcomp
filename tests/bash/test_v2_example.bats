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
    COMP_WORDS=("$@")
    COMP_LINE="$@"
    COMP_POINT=$((${#COMP_LINE} + 1))
    COMP_CWORD=${#COMP_WORDS[@]}

    echo Before: >$log_filename
    output_state >>$log_filename

    _cliname "$1"
}

assert_eq() {
    local expected=$@

    [[ "${COMPREPLY[@]}" == "$expected" ]] || {
        echo Error: >>$log_filename
        output_state >>$log_filename

        echo "Expected:" >>$log_filename
        echo "$expected" >>$log_filename

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
