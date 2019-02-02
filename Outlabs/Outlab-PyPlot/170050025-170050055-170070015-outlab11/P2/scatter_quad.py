import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
if __name__=="__main__":
	data=np.genfromtxt("3dpd.out",delimiter=",")
	a=2.3
	b=0.3
	c=-4
	red=np.array([x for x in data if (a*x[2]+b*(x[0]*x[0]+x[1]*x[1])+c)>=0])
	blue=np.array([x for x in data if (a*x[2]+b*(x[0]*x[0]+x[1]*x[1])+c)<0])
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(red[:,0],red[:,1],red[:,2],c='r')
	ax.scatter(blue[:,0],blue[:,1],blue[:,2],c='b')
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	ax.set_title("Quadratic Classifier")
	plt.show()
