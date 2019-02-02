import sqlite3
import csv

if __name__ == "__main__":
    ipl =sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    cur.execute('''SELECT Count(ball_id),striker, 'player'.player_name , count(distinct match_id)FROM 'BALL_BY_BALL' Join 'player' on 'player'.player_id='ball_by_ball'.striker group by striker   ORDER BY count(ball_id) DESC''')
    d1=cur.fetchall()
    rank=0
    prev=0
    list_avg=[]
    for a in d1:
    	c=[a[0]/a[3],a[1],a[2] ]
    	list_avg.append(c)
    list_avg.sort(key= lambda x: x[0], reverse= True)
    rank=0
    prev=list_avg[9][0]
    for a in list_avg:
    	rank+=1
    	#print(rank)
    	if rank > 10:
    	    break
    	if rank < 10:
    		print(str(a[1])+","+str(a[2])+","+str(a[0]))
    	if rank==10 and prev==a[0]:
    		print(str(a[1])+","+str(a[2])+","+str(a[0]))
    		rank-=1