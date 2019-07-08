import quandl
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

xs=np.array([1,2,3,4,5,6],dtype=np.float64)
ys=np.array([5,4,6,5,6,7],dtype=np.float64)

def dataset(hm,variance,step=2,correlation=False):
	val=1
	ys=[]
	for i in range(hm):
		y=val+random.randrange(-variance,variance)
		ys.append(y)
		if correlation and correlation=='pos':
			val+=step
		elif correlation and correlation=='neg':
			val-=step
	xs=[i for i in range (len(ys))]

	return np.array(xs,dtype=np.float64),np.array(ys,dtype=np.float64)


def bfitsl(xs,ys):
	m=(((mean(xs)*mean(ys))-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs*xs)))
	b=mean(ys)-m*mean(xs)
	return m,b


def error(ys_orig,ys_line):
	return sum((ys_line-ys_orig)**2)

def coff(ys_orig,ys_line):
	ys_mean_line=[mean(ys_orig) for y in ys_orig]
	er=error(ys_orig,ys_line)
	error_y_mean=error(ys_orig,ys_mean_line)
	return 1-(er/error_y_mean)

xs,ys=dataset(40,10,2,correlation='pos')


m,b=bfitsl(xs,ys)

line=[(m*x)+b for x in xs]

p_x=8
p_y=(m*p_x)+b

r_squred=coff(ys,line)
print(r_squred)

plt.scatter(xs,ys)
plt.scatter(p_x,p_y,s=100,color='green')
plt.plot(xs,line)
plt.show()


#Now we need to claculate R Squared value/error
