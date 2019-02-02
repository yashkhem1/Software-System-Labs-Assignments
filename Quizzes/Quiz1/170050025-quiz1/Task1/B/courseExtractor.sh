#! /bin/bash

wget -O temp.pdf $1
pdftotext temp.pdf
sed -i 's/Total Credits/Total credits/g' temp.txt
touch courses.txt
echo "Course Code " >> courses.txt
cat temp.txt |grep '^CS ***'| sed -e 's|\(CS ...\).*|\1 |g'| cat >> courses.txt
touch courseName.txt
echo " Course Name " >> courseName.txt
cat temp.txt |grep '^CS ***'| sed -e 's|.*: \(.*\).*| \1 |g'| cat >> courseName.txt
touch credits.txt
echo " Total Credits " >> credits.txt
cat temp.txt |grep '^Total credits'| sed -e 's|.*: \(.*\).*| \1 |g' | cat >> credits.txt
touch instructor.txt
echo " Instructor" >> instructor.txt
cat temp.txt |grep '^Instructor'| sed -e 's|.*: \(.*\).*| \1|g' | cat >> instructor.txt
paste -d "|" courses.txt courseName.txt credits.txt instructor.txt
rm temp.pdf temp.txt courses.txt courseName.txt credits.txt instructor.txt

