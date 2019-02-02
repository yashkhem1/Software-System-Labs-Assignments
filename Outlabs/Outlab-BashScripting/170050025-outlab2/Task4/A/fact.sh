#! /bin/bash

num=$1
re='^[0-9]+$'

factorial () {
   # else [[  $1 =~ $re ]]; then
   if [ $1 = 0 ]; then
        return 1
   else
        factorial $(( $1 -1 ))
        return $(( $1 * $? ))
    fi
}

if  [[ $1 =~ $re ]]; then
    factorial $1
    echo "$?"
else
    exit 1
fi
