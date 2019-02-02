#! /bin/bash

re='^[1-9][0-9]*$'
# read yourname
# echo $yourname
# if  [ ! $yournumber =~ $re ] ; then
#    echo "error: Not a number" >&2; exit 1
# fi


if  ! [[  $1 =~ $re ]]; then
    echo "Invalid argument!"
elif [[ $(( $1 % 100 )) = 0 && $(( $1 % 400 )) != 0 ]]; then
    echo "Not a leap year."
elif [ $(( $1 % 4 )) = 0 ]; then
    echo "Leap year!"
else
    #[ $(( $1 % 4 )) != 0 ]; then
    echo "Not a leap year."
#else
#    echo "Invalid argument!"
fi
