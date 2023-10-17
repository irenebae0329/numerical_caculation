import numpy as np
from function.poly_interpolation import *
from function.cubic_spline_interpolation import *
import matplotlib.pyplot as plt
x_list=np.linspace(-5,5,1000)
def f(x):
    return 1/(1+x**2)
x_p=np.linspace(-5,5,11)
x_c=np.linspace(-5,5,11)
y_p=np.array([f(x) for x in x_p])
y_c=np.array([f(x) for x in x_c])
expression_p=poly_interpolation(x_p,y_p)
expression_c=poly_interpolation(x_c,y_c)
y_m_p=np.array([expression_p.evalf(subs={'x':x_list[i]}) for i in range(1000)])
y_m_c=np.array([expression_c.evalf(subs={'x':x_list[i]}) for i in range(1000)])
y_ori=np.array([f(x) for x in x_list])

def plot():
    plt.plot(x_list,y_m_p,label='10次多项式插值')
    plt.plot(x_list,y_m_c,label='三次样条插值') 
    plt.plot(x_list,y_ori,label='原函数')
    plt.legend(loc='upper right')
    plt.show()

if __name__=='__main__':
    plot()    
