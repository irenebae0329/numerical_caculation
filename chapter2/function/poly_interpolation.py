import numpy as np
import sympy 
x=sympy.Symbol('x')
def poly_interpolation(x_list,y_list):
    assert len(x_list)==len(y_list),"x和y维度不相同"
    y_array=np.array(y_list)
    mat=[]
    for a in x_list:
        row=[]
        for i in range(len(x_list)):
            row.append(a**i)
        mat.append(row)
    mat=np.array(mat)
    a=np.linalg.inv(mat)@y_array.tolist()
    global x
    expression=sum([ a[i]*x**i for i in range(len(x_list))])
    return expression
