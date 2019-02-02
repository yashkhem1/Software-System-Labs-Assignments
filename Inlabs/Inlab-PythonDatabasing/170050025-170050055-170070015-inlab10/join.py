import sqlite3
import csv

if __name__=="__main__":
	pokedex =sqlite3.connect("pokedex.db")
	cur = pokedex.cursor()
	cur.execute('''SELECT pokemon.identifier,abilities.identifier FROM 'POKEMON',pokemon_abilities,abilities where pokemon.id=pokemon_abilities.pokemon_id and pokemon_abilities.ability_id=abilities.id order by pokemon.identifier,abilities.identifier''')
	i=0
	prev=''
	abilities=[]
	f=0
	for row in cur:
		if f==0:
			prev=row[0]
			f=1
		if row[0]!=prev:
			printer=''
			printer+=prev
			printer+='=['
			for a in abilities:
				printer+=a
				printer+=','
			printer=printer[:-1]
			printer+=']'
			print(printer)
			prev=row[0]
			abilities=[]
			abilities.append(row[1])
		else:
			abilities.append(row[1])
