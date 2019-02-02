import sqlite3

if __name__ == "__main__":
    ipl = sqlite3.connect("ipl.db")
    sixes = ipl.cursor()
    sixes.execute('''SELECT striker, 'player'.player_name, count(ball_id) FROM 'BALL_BY_BALL' Join 'player' on 'player'.player_id='ball_by_ball'.striker where runs_scored = 6  group by striker ''')
    balls = ipl.cursor()
    balls.execute('''SELECT striker,'player'.player_name, count(ball_id) FROM 'BALL_BY_BALL' Join 'player' on 'player'.player_id='ball_by_ball'.striker group by striker ''')
    d1 = sixes.fetchall()
    d2 = balls.fetchall()
    list_fraction = []
    for b in d2:
        f = 0
        for a in d1:
            if b[0] == a[0]:
                c = [a[0], a[1], a[2], b[2], a[2] * 1.0 / b[2]]
                list_fraction.append(c)
                f = 1
                break
        if f == 0:
            c = [b[0], b[1], 0, b[2], 0.0]
            list_fraction.append(c)
    list_fraction.sort(key=lambda x: x[4], reverse=True)
    for item in list_fraction:
        print(str(item[0]) + "," + item[1] + "," + str(item[2]) + "," + str(item[3]) + "," + str(item[4]))
