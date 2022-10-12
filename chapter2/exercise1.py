from turtle import color
from function.newton_interpolation import *
from function.cubic_spline_interpolation import *
import matplotlib.pyplot as plt 
expression=newton_interpolation([0.2,0.4,0.6,0.8,1.0],[0.98,0.92,0.81,0.64,0.38])
for i in [0,1,11,10]:
    xi=0.2+0.08*i
    yi=expression.evalf(subs={x:xi})
    yi1=main(xi,[0.2,0.4,0.6,0.8,1.0],[0.98,0.92,0.81,0.64,0.38])
    plt.scatter(xi,yi,color='r',label='牛顿插值')
    plt.scatter(xi,yi1,color='b',label='样条插值')
plt.show()