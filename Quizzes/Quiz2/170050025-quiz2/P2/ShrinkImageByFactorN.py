import numpy as np

def ShrinkImageByFactorN(img_mat, d):
	shrink_img = img_mat
    ## Write code below this
	array1=[];
	nrows = img_mat.shape[0]
	ncolums = img_mat.shape[1]
	i=0
	while i< nrows:
		array1.append(img_mat[i])
		i = i + d
	
	
	shrink_img = np.array(array1)

	array2 = []
	i = 0

	nrows = shrink_img.shape[0]

	while i < nrows:
		j = 0
		mlist = []
		while j < ncolums:
			mlist.append(shrink_img[i][j])
			j = j+d

		array2.append(mlist)
		i = i + 1

	shrink_img = np.array(array2)

    # shrink_img = shrink_img[0:d:,:]
    # shrink_img = shrink_img[:,0:d:]
    ## Donot change anything else
	return shrink_img


# if __name__=="__main__":
# 	mat = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
# 	print(ShrinkImageByFactorN(mat,3))

