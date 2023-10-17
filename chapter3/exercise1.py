import numpy as np
import sympy 
from function.least_square_fit import *
x=sympy.Symbol('x')
def f(x):
    return 1/math.sqrt(1+x**2)
xlist=[ -1+0.2*i for i in range(11)]
ylist=[ f(x) for x in xlist]
#print(x_list,y_list)
expression=least_square_fit(xlist,ylist,3)
x_list=np.linspace(-1,1,1000)
y_list=[f(x) for x in x_list]
yf_list=[expression.evalf(subs={x:a}) for a in x_list]
plt.plot(x_list,y_list)
plt.plot(x_list,yf_list)
plt.show()