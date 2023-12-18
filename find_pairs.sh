#!/bin/bash

count_pairs_with_condition() {
    local n=$1
    local -arr arr=("${@:2}")
    local count=0

    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < n; j++)); do
            if [[ $i -ne $j && ${arr[i]} -eq $((arr[j] + i - j)) ]]; then
                ((count++))
            fi
        done
    done

    echo $count
}

read -p "" n
read -p "" -a arr

result=$(count_pairs_with_condition $n "${arr[@]}")
echo $result
