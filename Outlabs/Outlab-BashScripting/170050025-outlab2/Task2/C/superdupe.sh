#! /bin/bash

Dirname=`dirname $2`

mkdir -p $Dirname

if [ ! -f $2 ]; then
    cp $1 $2
    echo "Copied $1"
else
    echo "Not copied $1"
fi
