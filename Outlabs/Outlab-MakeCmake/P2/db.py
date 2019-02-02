#! python3
import csv
import sqlite3

# cse_students.sqlite


def makeDB():
    file = open('count.csv', 'r')
    reader = csv.reader(file, delimiter='\t', quotechar=' ')

    conn = sqlite3.connect('cse_students.sqlite')
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS Students")
    c.execute("CREATE TABLE Students([Category Name] text, [No. of students] real)")

    for row in reader:
        if row[0] == 'Category Name':
            continue
        else:
            c.execute("INSERT INTO Students VALUES('" + str(row[0]) + "'," + str(row[1]) + ")")

    conn.commit()
    conn.close()
    file.close()


def returnCount():
    try:
        category = input()
        conn = sqlite3.connect('cse_students.sqlite')
        c = conn.cursor()

        c.execute("SELECT [No. of students] FROM Students WHERE [Category Name] ='" + str(category) + "'")
        print(int(c.fetchone()[0]))

    except TypeError:
        print('Enter Correct Category')

if __name__ == "__main__":
    makeDB()
    returnCount()
