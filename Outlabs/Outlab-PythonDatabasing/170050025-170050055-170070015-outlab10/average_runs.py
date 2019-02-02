import sqlite3
import csv

if __name__ == "__main__":
    ipl = sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    cur.execute('''SELECT sum(runs_scored),venue_name from 'ball_by_ball'  Join 'match' on 'match'.match_id='ball_by_ball'.match_id group by 'match'.venue_name ''')
    ginti = ipl.cursor()
    ginti.execute('''select  count(match_id), venue_name  from 'match' where venue_name!="NULL" group by venue_name ''')
    d1 = cur.fetchall()
    d2 = ginti.fetchall()
    list_average = []
    for a in d1:
        for b in d2:
            if b[1] == a[1]:
                c = [a[1], a[0] / b[0]]
                list_average.append(c)
                break
    list_average.sort(key=lambda x: x[1], reverse=True)
    for item in list_average:
        print(str(item[0]) + "," + str(item[1]))
