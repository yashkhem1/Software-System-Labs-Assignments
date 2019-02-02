import csv
import matplotlib.pyplot as plt
import numpy as np
if __name__=="__main__":
	file=open("survey_data.csv","r")
	r=csv.reader(file)
	data=list(r)
	topics=data[0]
	topics=topics[1:]
	count_for_topics=[]
	for x in topics:
		# ‘’, ‘’, ‘’, ‘’
		dict={'Essential':0,'Dont care one way or another':0,'Nice to have':0,'Utterly useless':0}
		count_for_topics.append(dict)
	# print(data)
	for x in data[1:]:
		# print(x)
		for i in range(1,len(topics)+1):
			count_for_topics[i-1][x[i]]+=1
	essentials=[]
	dont_care=[]
	nice=[]
	useless=[]
	for x in count_for_topics:
		essentials.append(x["Essential"])
		dont_care.append(x['Dont care one way or another'])
		nice.append(x['Nice to have'])
		useless.append(x['Utterly useless'])
		# print(x["Essential"]+x['Dont care one way or another']+x['Nice to have']+x['Utterly useless'])
	ind = np.arange(len(topics))
	width = 0.5
	p1 = plt.bar(ind, essentials, width,color='r')
	p2 = plt.bar(ind, dont_care, width,bottom=essentials,color='b')
	p3 = plt.bar(ind, nice, width,bottom=np.array(dont_care)+np.array(essentials),color='g')
	p4 = plt.bar(ind,useless,width,bottom=np.array(nice)+np.array(essentials)+np.array(dont_care),color='c')
	xlabels=["Bash","csh/tsh/zsh","Unix System Tools","RegEx-python","RegEx-awk, sed","Perl Programming","Python-base language","Python-os, sys.. ","Python-csv, pickle..","Python-numpy, scipy..","Python-networking, requests","Java-language, package, class..","Java-Concurrency","Java-Networking","Java-JNI","Java-JDBC","Version Control-svn","Version Control-git","IDE-Eclipse","IDE-Jetbrains PyCharm, Java","IDE-NetBeans","Build Environments" ,"Client Side","Server Side","Latex..","Lex and Yacc","Erlang","MPI"]
	plt.legend((p1[0], p2[0],p3[0],p4[0]), ('Essential', 'Don\'t Care','Nice To Have','Utterly Useless'))
	plt.xticks(ind, xlabels, rotation='270')
	plt.yticks(np.arange(0, 20, 1))
	plt.xlabel("Topics")
	plt.ylabel("Opinions")
	plt.title("Opinion Histogram")
	#plt.show()
	plt.savefig("hists.png",bbox_inches='tight')
	# print(essentials)
	# print(dont_care)
	# print(nice)
	# print(useless)
