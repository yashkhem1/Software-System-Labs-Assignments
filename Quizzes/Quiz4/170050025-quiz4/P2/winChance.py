import sqlite3

if __name__=="__main__":
	ipl = sqlite3.connect("ipl.db")
	total = ipl.cursor()
	first = ipl.cursor()
	second = ipl.cursor()
	total.execute("Select count(battedfirst) from match where battedfirst!='NULL'")
	first.execute("Select count(battedfirst) from match where battedfirst!='NULL' and match_winner!='NULL' and battedfirst = match_winner")
	second.execute("Select count(battedfirst) from match where battedsecond!='NULL' and match_winner!='NULL' and battedsecond = match_winner")
	totalMatches=list(total.fetchall())[0][0]
	battedFirst=list(first.fetchall())[0][0]
	battedSecond = list(second.fetchall())[0][0]
	p1= battedFirst*1.0/totalMatches
	p2= battedSecond*1.0/totalMatches
	print(round(p1,3))
	print(round(p2,3))
	# print(totalMatches)
	ipl.close()