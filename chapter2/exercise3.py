import numpy as np
from function.poly_interpolation import *
from function.cubic_spline_interpolation import *
import matplotlib.pyplot as plt
#第一问
x_1=[0,1,4,9,16,25,36,49,64]
y_1=[0,1,2,3,4,5,6,7,8]
x_list=np.linspace(0,64,10000)
expression=poly_interpolation(x_1,y_1)
#第二问
y_m=np.array([expression.evalf(subs={'x':x_list[i]}) for i in range(10000)])
y_c=np.array([main(x_list[i],x_1,y_1) for i in range(10000)])
print(y_c)
plt.plot(x_list,y_c)
plt.plot(x_list,y_m)
plt.scatter(x_1,y_1)
plt.show()