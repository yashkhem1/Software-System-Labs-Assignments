import numpy as np 
def ang_to_vec(ang):
	vec=np.zeros((len(ang),2))
	ang=np.deg2rad(ang)
	sins=np.sin(ang)
	coss=np.cos(ang)
	vec=np.c_[coss,sins]
	return(vec)

def vec_to_ang(vec):
	# print(vec)
	return np.rad2deg(np.arctan2(vec[:,1],vec[:,0])).reshape((vec.shape[0],1))