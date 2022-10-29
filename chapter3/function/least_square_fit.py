import sympy 
import matplotlib.pyplot as plt
import numpy as np
import math
x=sympy.Symbol('x')
def least_square_fit(x_list,y_list,degree):
    assert len(x_list)==len(y_list),"x,y维度不同"
    #degree=len(x_list)
    degree=degree
    p_list,a_list=[],[]
    def inner_product(expression_1,expression_2):
        if type(expression_1)==int and type(expression_2)==int:
            return sum([expression_1*expression_2 for i in range(len(x_list))])
        elif (type(expression_1)==type([]))^(type(expression_2)==type([])):
            num=expression_1 if type(expression_1)==int else expression_2
            list_1=expression_1 if type(expression_1)==type([]) else expression_2
            try:
                return sum([ list_1[i]*num.evalf(subs={x:x_list[i]}) for i in range(len(x_list))])
            except:
                return sum([ list_1[i]*num for i in range(len(x_list))])
        elif type(expression_1)==int and type(expression_2)==int:
            return sum(list(map(lambda a,b:a+b,x_list,y_list)))
        return sum([(expression_1*expression_2).evalf(subs={x:x_list[i]}) for i in range(len(x_list))])
    def p(k):
        if k==0:
            return 1
        elif k==1:
            return (x-alpha(k))*p_list[k-1]
        else:
            return (x-alpha(k))*p_list[k-1]-beta(k)*p_list[k-2]
    def alpha(k):
        a=inner_product(x*p_list[k-1],p_list[k-1])
        b=inner_product(p_list[k-1],p_list[k-1])
        return a/b
    def beta(k):
        return inner_product(p_list[k-1],p_list[k-1])/inner_product(p_list[k-2],p_list[k-2])
    def alpha_star(k):
        return inner_product(y_list,p_list[k])/inner_product(p_list[k],p_list[k])
    for k in range(degree):
        p_list.append(p(k))
    for k in range(degree):
        a_list.append(alpha_star(k))
    print(p_list,a_list)
    return sum(list(map(lambda x,y:x*y,p_list,a_list)))
