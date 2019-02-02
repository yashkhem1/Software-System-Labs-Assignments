import sqlite3

if __name__ == "__main__":
    pokedex =sqlite3.connect("pokedex.db")
    cur = pokedex.cursor()
    cur.execute('''CREATE TABLE POKEMON (id int,
    identifier varchar(10), species varchar(10), height int,weight int,base_experience int, order1 int , is_default int)''')

    cur.execute('''CREATE TABLE POKEMON_ABILITIES (pokemon_id int,
    ability_id int,is_hidden int,slot int)''')

    cur.execute('''CREATE TABLE ABILITIES (id int,
    identifier varchar(10), generation_id int,is_main_series int)''')