_mc_autocomp() {
    local cur prev opts
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_LINE%$cur}"

    opts="$(mc_autocomp "$prev" "$cur")"  # 运行 `mc autocomp` 并获取补全列表

    COMPREPLY=()
    if [[ -n $opts ]]; then
        COMPREPLY=( $(compgen -W "$opts" -- "$cur") )  # 使用 `compgen` 生成补全列表
    fi
}
complete -F _mc_autocomp mc
