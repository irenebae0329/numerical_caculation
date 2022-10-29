from function.least_square_fit import *
import matplotlib.pyplot as plt
import numpy as np
x_list=[0.0,0.1,0.2,0.3,0.5,0.8,1.0]
y_list=[1.0,0.41,0.50,0.61,0.91,2.02,2.46]
expression_3=least_square_fit(x_list,y_list,4)
expression_4=least_square_fit(x_list,y_list,5)
point_list=np.linspace(0,1,1000)
y_3=[expression_3.evalf(subs={x:a}) for a in point_list]
y_4=[expression_4.evalf(subs={x:a}) for a in point_list]
plt.plot(point_list,y_3,'r')
plt.plot(point_list,y_4,'b')
plt.show()