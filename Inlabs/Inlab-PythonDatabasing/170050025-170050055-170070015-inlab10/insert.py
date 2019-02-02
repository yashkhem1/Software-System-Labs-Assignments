import sqlite3
import csv

if __name__=="__main__":
	pokedex =sqlite3.connect("pokedex.db")
	cur = pokedex.cursor()
	file=open('pokemon.csv')
	reader=csv.reader(file)
	data=list(reader)
	cur.executemany('''insert into pokemon values(?,?,?,?,?,?,?,?)''',data[1:])
	file=open('abilities.csv')
	reader=csv.reader(file)
	data=list(reader)
	cur.executemany('''insert into Abilities values(?,?,?,?)''',data[1:])
	file=open('pokemon_abilities.csv')
	reader=csv.reader(file)
	data=list(reader)
	cur.executemany('''insert into pokemon_abilities values(?,?,?,?)''',data[1:])
	pokedex.commit()
	pokedex.close()