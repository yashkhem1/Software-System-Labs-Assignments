#! /bin/bash

oldfile=$1
newfile=$2
checkfile="$newfile"".md5"

cat $oldfile | tee >(md5sum > $checkfile) | cat > $newfile
sed -i "s#-#$newfile#" $checkfile
md5sum -c $checkfile
