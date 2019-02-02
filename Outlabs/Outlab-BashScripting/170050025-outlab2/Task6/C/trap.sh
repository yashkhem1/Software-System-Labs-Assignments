#! /bin/bash

csv=$1

foo () {
    awk -f lure.awk $csv >> loki.csv
    exit
}

while :
    do
        trap 'foo' 2
    done
