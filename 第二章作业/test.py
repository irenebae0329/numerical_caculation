import numpy as np
def f1(j,x):
    return 1*attr_list[j]
def f2(x):
    return 2
attr_list=[1,2,3,4]
x=np.linspace(0,3,2)
f_list=[]
for i in range(2):
    f_list.append(lambda x:x>i)


np.piecewise(x,f_list,[f1,f2])