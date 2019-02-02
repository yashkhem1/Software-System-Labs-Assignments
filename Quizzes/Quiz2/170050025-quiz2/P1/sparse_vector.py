
class SparseVector:

    def __init__(self, N):
    	
		if isinstance(N,float):
			raise ValueError
		
		if isinstance(N,str):
			try:
				N = int(N)
			except:
				raise ValueError

		if N < 0:
			raise ValueError
		else:
			self.N = N
	        self.values = dict()

		




    def __setitem__(self, key, item):

    	if isinstance(key,float):
    		raise TypeError

    	if isinstance(key,str):
    		try:
    			key = int(key)
    		except :
    			raise TypeError

    	key = int(key)
    	if key not in range(0,self.N):
    		raise IndexError
        self.values[key] = item



    def __getitem__(self, key):

    	if isinstance(key,float):
    		raise TypeError

    	if isinstance(key,str):
    		try:
    			key = int(key)
    		except :
    			raise TypeError

    	key = int(key)
    	if key not in range(0,self.N):
    		raise IndexError


    	if key in list(self.values.keys()):
        	return self.values[key]

        else:
        	return 0

# if __name__=="__main__":
# 	a = SparseVector("40")
# 	a[0] = 34
# 	a["35"] = 56
# 	temp = a["35"]
# 	print(temp)
# 	#a[10] = 0
# 	#print(a[10])
# 	#a = SparseVector("Hello")
