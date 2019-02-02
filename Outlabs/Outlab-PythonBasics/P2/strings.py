file=open('employees.txt')
text=file.read().split('\n')
for line in text:
	name=line.split(' ')[0]
	cat=name[3:]+name[0:3]
	print(cat)