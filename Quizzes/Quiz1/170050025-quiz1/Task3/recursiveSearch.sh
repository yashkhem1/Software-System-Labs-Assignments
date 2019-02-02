#! /bin/bash

if [ $# = 0 ]; then
    echo "Usage: ./recursiveSearch.sh <words-to-search>"
    exit 1
fi

out=0

for i in $*
do
    if [ $i = $1 ];then
        out=$(grep -i -n -r $i Data)
    else
        out=$(echo "$out" | grep -i $i)
    fi
done

echo "$out"
