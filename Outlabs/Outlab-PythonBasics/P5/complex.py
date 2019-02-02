import sys
class Complex(object):
	"""docstring for Complex"""
	def __init__(self, real, img):
		#super(Complex, self).__init__()
		self.real = real
		self.img = img

	def __str__(self):
		if (self.img < 0):
			return(str(self.real)+str(self.img)+"i" )
		else:
			return(str(self.real)+"+"+str(self.img)+"i")

	def __add__(self,another):
		a=self.real+another.real
		b=self.img+another.img
		return Complex(a,b)

	def __sub__(self,another):
		a=self.real-another.real
		b=self.img-another.img
		return Complex(a,b)

	def __mul__(self,another):
		r=self.real*another.real - self.img*another.img
		i=self.img*another.real + self.real*another.img
		return Complex(r,i)

	def __truediv__(self,another):
		if another.img==0:
			if another.real!=0:
				return Complex(self.real/another.real, self.img/another.real)
			else:
				raise ValueError('Division by Zero')
		else:
			r=self.real*another.real + self.img*another.img
			i=self.img*another.real-self.real*another.img
			d=another.real**2+another.img**2
			return Complex(r/d,i/d)

if __name__ == '__main__':
	with open("numbers.txt") as infile:
		lines=infile.readlines()
		c=[]
		for l in lines:
			a=[float(x) for x in l.split()]
			print(a)
			c.append(a)

	c1=Complex(c[0][0],c[0][1])
	c2=Complex(c[1][0],c[1][1])
	print(c1)
	print(c2)
	print(c1+c2)
	#add.__str__()
	print(c1-c2)
	print(c1*c2)
	print(c1/c2)
