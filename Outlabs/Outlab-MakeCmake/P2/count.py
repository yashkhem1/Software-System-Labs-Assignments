#! python3
import requests
import bs4
import csv

if __name__ == "__main__":
    link = 'https://www.cse.iitb.ac.in/page222'
    res = requests.get(link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select('div[class="mpart"] li > a')

    with open('count.csv', 'w') as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(['Category Name', 'No. of students'])
        for elem in elems:
            name = elem.getText()
            linkElem = elem.get('href')
            linkElem = link + linkElem
            res1 = requests.get(linkElem)
            res1.raise_for_status()
            soup1 = bs4.BeautifulSoup(res1.text, "html.parser")
            studentRow1 = soup1.select('table tr[class="row1"]')
            studentRow2 = soup1.select('table tr[class="row2"]')
            count = 0
            for student in studentRow1 + studentRow2:
                if 'TEMPLATE' not in student.text:
                    count = count + 1
            writer.writerow([name, count])
