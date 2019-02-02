BEGIN {
    FS = ","  
}

(NR!=1 && $4 >= 2000) {tess [$3] += $5}

END {
    for (x in tess)
        print x ", " tess[x] | "sort"
}


