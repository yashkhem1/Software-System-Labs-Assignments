import PIL.Image
import numpy as np
import sys
import scipy.misc

def norm(p1,p2):
	return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 )**0.5
def euclid(point,mean_lake,mean_veg,mean_built,mean_sea):
	d=[[norm(point,mean_sea),0],[norm(point,mean_lake),75],[norm(point,mean_built),255],[norm(point,mean_veg),128]]
	# print(sorted(d))
	return sorted(d)[0][1]

def man_dist(p1,p2):
	return(np.sum(np.abs(p2-p1)))

def manhattan(point,mean_lake,mean_veg,mean_built,mean_sea):
	d=[(man_dist(point,mean_sea),0),(man_dist(point,mean_lake),75),(man_dist(point,mean_built),255),(man_dist(point,mean_veg),128)]
	# print(d)
	return sorted(d)[0][1]

if __name__=="__main__":
	if(len(sys.argv)>2 or len(sys.argv)==1 or (sys.argv[1]!="eu" and sys.argv[1]!="man")):
		print("Unknown option")
	else:

		mean_lake=np.zeros((3,1))
		mean_veg=np.zeros((3,1))
		mean_built=np.zeros((3,1))

		sea_r=np.zeros((1,1))
		sea_b=np.zeros((1,1))
		sea_g=np.zeros((1,1))
		for x in ['sea1.png','sea2.png','sea3.png']:
			I = np.asarray(PIL.Image.open(x))
			sea_r=np.append(sea_r,I[:,:,0].ravel())
			sea_b=np.append(sea_b,I[:,:,1].ravel())
			sea_g=np.append(sea_g,I[:,:,2].ravel())
		#print(sea_b)
		mean_sea = np.array([np.mean(sea_r[1:]),np.mean(sea_b[1:]),np.mean(sea_g[1:])])
		sea_r=np.zeros((1,1))
		sea_b=np.zeros((1,1))
		sea_g=np.zeros((1,1))
		for x in ['vegetation1.png','vegetation2.png','vegetation3.png','vegetation4.png']:
			I = np.asarray(PIL.Image.open(x))
			sea_r=np.append(sea_r,I[:,:,0].ravel())
			sea_b=np.append(sea_b,I[:,:,1].ravel())
			sea_g=np.append(sea_g,I[:,:,2].ravel())
		mean_veg=np.array([np.mean(sea_r[1:]),np.mean(sea_b[1:]),np.mean(sea_g[1:])])
		sea_r=np.zeros((1,1))
		sea_b=np.zeros((1,1))
		sea_g=np.zeros((1,1))
		x = 'builtup.png'
		I = np.asarray(PIL.Image.open(x))
		sea_r=np.append(sea_r,I[:,:,0].ravel())
		sea_b=np.append(sea_b,I[:,:,1].ravel())
		sea_g=np.append(sea_g,I[:,:,2].ravel())
		mean_built=np.array([np.mean(sea_r[1:]),np.mean(sea_b[1:]),np.mean(sea_g[1:])])
		sea_r=np.zeros((1,1))
		sea_b=np.zeros((1,1))
		sea_g=np.zeros((1,1))
		x = 'lake.png'
		I = np.asarray(PIL.Image.open(x))
		sea_r=np.append(sea_r,I[:,:,0].ravel())
		sea_b=np.append(sea_b,I[:,:,1].ravel())
		sea_g=np.append(sea_g,I[:,:,2].ravel())
		mean_lake=np.array([np.mean(sea_r[1:]),np.mean(sea_b[1:]),np.mean(sea_g[1:])])
		#print(mean_built,mean_veg,mean_sea,mean_lake)
		I = np.asarray(PIL.Image.open('mumbai.png'))
		result=np.zeros((I.shape[0],I.shape[1]))
		for i in range(result.shape[0]):
			for j in range(result.shape[1]):
				if sys.argv[1]=='eu':
					# print(I[i][j])
					# print(mean_sea)
					result[i][j]=euclid(I[i][j],mean_lake,mean_veg,mean_built,mean_sea)
				else:
					result[i][j]=manhattan(I[i][j],mean_lake,mean_veg,mean_built,mean_sea)
		if sys.argv[1]=="eu":
			scipy.misc.imsave('segmented_eu.png',result)
		else:
			scipy.misc.imsave('segmented_man.png',result)




