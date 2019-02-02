import sqlite3
import sys

if __name__ == "__main__":
    # arg=sys.argv[1]
    ipl = sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    inp = input()
    choice = input()
    # args=arg.splitlines()
    if(choice == '0'):
        # for a in args[1:]:
        # 	try:
        # 		values.append(int(a))
        # 	except:
                    # values.append(a)
        table_dict = {'1': 'team', '2': 'player', '3': 'match'}
        column_dict = {'1': "team_name = '", '2': "player_name = '", '3': "match_id = '"}
        end_dict = {'1': '"', '2': '"', '3': ''}
        s = input()
        command = 'delete from ' + table_dict[inp] + ' where ' + column_dict[inp] + s + "'"
        # print(command)
        cur.execute(command)
        ipl.commit()
        ipl.close()
    else:
        table_dict = {'1': 'team', '2': 'player', '3': 'match'}
        column_dict = {'1': 'team_name = ?', '2': 'player_name = ?', '3': 'match_id = ?'}
        s = input()
        try:
            p = int(s)
        except:
            p = s

        command = 'delete from ' + table_dict[inp] + ' where ' + column_dict[inp]
        # print(command,p)
        cur.execute(command, (p,))
        ipl.commit()
        ipl.close()
