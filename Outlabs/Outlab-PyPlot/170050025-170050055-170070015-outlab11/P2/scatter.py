import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
if __name__=="__main__":
    data=np.genfromtxt("3dpd.out",delimiter=",")
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(data[:,0],data[:,1],data[:,2])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Scatter Plot")
    plt.show()
