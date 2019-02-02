import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
if __name__=="__main__":
	data=np.genfromtxt("3dpd.out",delimiter=",")
	a=1
	b=-1.3
	red=np.array([x for x in data if (a*x[2]+b)>=0])
	blue=np.array([x for x in data if (a*x[2]+b)<0])
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(red[:,0],red[:,1],red[:,2],c='r')
	ax.scatter(blue[:,0],blue[:,1],blue[:,2],c='b')
	ax.set_title("Linear Classsifier")
	plt.show()
