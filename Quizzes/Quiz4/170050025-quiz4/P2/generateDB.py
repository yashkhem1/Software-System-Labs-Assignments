import sqlite3
import csv

if __name__=="__main__":
	ipl = sqlite3.connect("ipl.db")
	cur = ipl.cursor()
	cur.execute('''CREATE TABLE MATCH (match_id int, season_year int,   team1 int,  team2 int,  battedfirst int,
	battedsecond int,   venue_name text NOT NULL, city_name text, country_name text , toss_winner int,
	match_winner    int, toss_name text,    win_type text , man_of_match int,  win_margin int, primary key (match_id))''')
	file=open('match.csv')
	reader=csv.reader(file)
	data=list(reader)
	cur.executemany('''insert into match values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',data[1:])
	ipl.commit()
	# cur.execute("Select * from match")
	# print(list(cur.fetchall()))
	ipl.close()