#! /bin/bash

dir1=$1
dir2=$2

foo () {
    numelem=$#
    let i=1
    while [ $i -le $numelem ]
    do
       # echo "${!i} process"
        fdir1=${!i}
        fdir2=${fdir1/$dir1/$dir2}
       # echo $fdir1
       # echo $fdir2
        #echo ""
        #testdir=$1
        #echo "${testdir/$dir1/$dir2}"
        Dirname=`dirname $fdir2`

        mkdir -p $Dirname

        if [ ! -f $fdir2 ]; then
            cp $fdir1 $fdir2
            echo "Copied $fdir1"
        else
            echo "Not copied $fdir1"
        fi

        let i+=1
    done
}

foo $(find $dir1 -type f)
