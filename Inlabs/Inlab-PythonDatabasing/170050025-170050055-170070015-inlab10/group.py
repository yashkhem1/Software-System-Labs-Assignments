import sqlite3
import csv

if __name__=="__main__":
	pokedex =sqlite3.connect("pokedex.db")
	cur = pokedex.cursor()
	cur.execute('''SELECT max(base_experience) FROM 'POKEMON' group by species order by max(base_experience) desc''')
	i=0
	for row in cur:
		if(i<3):
			print(row[0])
			i+=1
		else:
			break
