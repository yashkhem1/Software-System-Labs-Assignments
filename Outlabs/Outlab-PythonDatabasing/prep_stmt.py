import sqlite3
# import sys

if __name__ == "__main__":
    # arg=sys.argv[1]
    ipl = sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    choice = input()
    len_dict = {'1': 2, '2': 6, '3': 15, '4': 7, '5': 11}
    values = []
    for i in range(len_dict[choice]):
        inp = input()
        # try:
        #     values.append(int(inp))
        # except:
        values.append(inp)
    table_dict = {'1': 'team', '2': 'player', '3': 'match', '4': 'player_match', '5': 'ball_by_ball'}
    # print(values)
    s = ',?' * len(values)
    s = '(' + s[1:] + ')'
    # print(s)
    command = 'insert into ' + table_dict[choice] + ' values' + s
    cur.execute(command, values)
    ipl.commit()
    ipl.close()
