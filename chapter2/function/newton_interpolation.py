import sympy 
x,t=sympy.symbols("x,t")
x0,x1,y0,y1,x2,y2=sympy.symbols("x0 x1 y0 y1 x2 y2")
#牛顿插值
def multiplicative_p(i,indice,x_list):
    if(i>=len(x_list)):
        return 1
    if(i!=indice):
        return (x_list[indice]-x_list[i])*multiplicative_p(i+1,indice,x_list)
    else:
        return 1*multiplicative_p(i+1,indice,x_list)
def multicaptive_v(x_list,n,k=0):
    if(k>=n or len(x_list)==0):
        return 1
    else:
        return (x-x_list[k])*multicaptive_v(x_list,n,k+1)
def param_degree_n(x_list,y_list,n):
    res=0
    for i in range(n):
        res+=y_list[i]*(1/multiplicative_p(0,i,x_list))
    return res
    
def difference_quotient(x_list:list,y_list:list,degree):
    if degree==1:
        return y_list[0]
    return param_degree_n(x_list,y_list,degree)
def newton_interpolation(x_list,y_list):
    assert len(x_list)==len(y_list)
    degree=len(x_list)
    param_list,var_list=[],[]
    for i in range(1,degree+1):
        param_list.append(difference_quotient(x_list[0:i],y_list[0:i],i))
        var_list.append(multicaptive_v(x_list[0:i-1],i-1))
    expression=sum(list(map(lambda x,y:x*y,param_list,var_list)))
    return expression
if __name__=='__main__':
    expression3=newton_interpolation([1,-1,2],[0,-3,4])
    result2_1=newton_interpolation([0.5,0.6,0.7],[-0.693147,-0.510826,-0.356675]).evalf(subs={x:0.54})
    print(result2_1)
    


        



