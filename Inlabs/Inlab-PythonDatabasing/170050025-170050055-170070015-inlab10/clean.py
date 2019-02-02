import sqlite3
import csv

if __name__=="__main__":
	pokedex =sqlite3.connect("pokedex.db")
	cur = pokedex.cursor()
	cur.execute('''DELETE FROM 'POKEMON' where identifier like "rogue%" ''')
	pokedex.commit()
	pokedex.close()