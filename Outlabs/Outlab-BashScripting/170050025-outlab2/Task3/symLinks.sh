#! /bin/bash

dir=$1
#echo $dir
file=$2
#echo $file
#echo "$file"

foo () {
    numelem=$#
   # echo $numelem
    let i=1

    while [ $i -le $numelem ]
    do
        fname=${!i}
        target=`readlink $fname`

        if [ -d $target ]; then
            echo -e "$fname $target @ 1" >> $file
    #        echo -e "$fname\t$target\t@\t1"
        else
            echo -e "$fname $target $( cut -d' ' -f1 <<< $( md5sum $target ) ) 0" >> $file
     #       echo -e "$fname\t$target\t$( cut -d' ' -f1 <<< $( md5sum $target ) )\t0"
        fi

        let i+=1
    done

    sort -o $file $file
}

foo $(find $dir -type l)
