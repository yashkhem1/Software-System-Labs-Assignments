#!/bin/bash
bank="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
str=""

c=${bank:$(($RANDOM%36)):1}
str+=$c
c=${bank:$(($RANDOM%36)):1}
str+=$c
c=${bank:$(($RANDOM%36)):1}
str+=$c
sed -e "s/[A-Z][A-Z][0-9]/$str/g" "$1"
