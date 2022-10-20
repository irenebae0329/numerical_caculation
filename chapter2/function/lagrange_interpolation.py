import sympy
x=sympy.Symbol("x")
x0,y0,x1,y1,x2,y2=sympy.symbols("x0,y0,x1,y1,x2,y2")
def multiplicative(i,indice,x_list):
    if(i>=len(x_list)):
        return 1
    if(i!=indice):
        return (x-x_list[i])/(x_list[indice]-x_list[i])*multiplicative(i+1,indice,x_list)
    else:
        return 1*multiplicative(i+1,indice,x_list)
           
def return_param_list(n,x_list):
    param_list=[]
    for i in range(n):
        param_list.append(multiplicative(0,i,x_list))
    return param_list
def Lagrange_interpolation(x_list,y_list):
    assert x_list,y_list
    n=len(x_list)
    param_list=return_param_list(n,x_list)
    expression=sum(list(map(lambda x,y:x*y,param_list,y_list)))
    return expression
if __name__=='__main__':
    expression1=Lagrange_interpolation([1,-1],[0,-3])
    expression2=Lagrange_interpolation([1,-1,2],[0,-3,4])
    #第二题
    result2_1=Lagrange_interpolation([0.5,0,6],[-0.693147,-0.510826]).evalf(subs={x:0.54})
    result2_2=Lagrange_interpolation([0.5,0.6,0.7],[-0.693147,-0.510826,-0.356675]).evalf(subs={x:0.54})
    print(result2_1,result2_2)