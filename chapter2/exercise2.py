import numpy as np
from function.poly_interpolation import *
from function.cubic_spline_interpolation import *
import matplotlib.pyplot as plt
x_list=np.linspace(-1,1,100)
def f(x):
    return 1/(1+25*x**2)
x_10=np.linspace(-1,1,10)
x_20=np.linspace(-1,1,20)
y_10=np.array([f(x) for x in x_10])
y_20=np.array([f(x) for x in x_20])
expression_10=poly_interpolation(x_10,y_10)
expression_20=poly_interpolation(x_20,y_20)
y_10_i=np.array([expression_10.evalf(subs={'x':x_list[i]}) for i in range(100)])
y_20_i=np.array([expression_20.evalf(subs={'x':x_list[i]}) for i in range(100)])
y_ori=np.array([f(x) for x in x_list])
fig = plt.figure()
plt.plot(x_list,y_10_i)
plt.plot(x_list,y_20_i)
plt.plot(x_list,y_ori)
plt.show()