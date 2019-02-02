#! /bin/bash
re='^[0-9]*$'
num=$1

factorial()
{
    if [ $1 = 0 ]; then
        echo 1
    else
        last=$(factorial $(( $1-1 )))
        echo $(($1 * last))
    fi
}

if [[ $num =~ $re ]]; then
    factorial $num
else
    exit 1
fi
