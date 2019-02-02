import sqlite3
import csv

if __name__=="__main__":
	pokedex =sqlite3.connect("pokedex.db")
	cur = pokedex.cursor()
	cur.execute('''update 'abilities' set generation_id=8 where is_main_series=0 ''')