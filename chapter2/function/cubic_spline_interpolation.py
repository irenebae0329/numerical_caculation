#三次样条插值
import sympy 
import matplotlib.pyplot as plt
import numpy as np
a=sympy.Symbol('a')
def cubic_spline_interpolation(x_list,y_list):
    assert len(x_list)==len(y_list) and len(x_list)>3
    degree=len(x_list)-1
    mat=np.zeros([degree+1,degree+1])
    def create_section_list(x_list):
        section_list=[]
        h_list=[]
        for i in range(degree):
            section_list.append((x_list[i],x_list[i+1]))
            h_list.append(x_list[i+1]-x_list[i])
        return section_list,h_list
    def equal_difference_n(i):
        return (y_list[i+1]-y_list[i])/(x_list[i+1]-x_list[i])
    def d(i):
        if i==0:
            return 0
        elif i==degree:
            return 0
        else:
            return 6*(equal_difference_n(i)-equal_difference_n(i-1))/(h_list[i-1]+h_list[i])
    def caculate_attr(x_list,y_list,h_list):
        d_list=[]
        for i in range(degree+1):
            mat[i][i]=2
            d_list.append(d(i))
            if i>=1 and i<=degree-1:
                mat[i][i-1],mat[i][i+1]=h_list[i-1]/(h_list[i-1]+h_list[i]),h_list[i]/(h_list[i]+h_list[i-1])
        return np.linalg.solve(mat,np.array(d_list))
    
    section_list,h_list=create_section_list(x_list)
    M=caculate_attr(x_list,y_list,h_list)
    s_dict_list=[]
    for i in range(len(section_list)):
        p1=np.divide(M[i],6*h_list[i])
        p2=np.divide(M[i+1],6*h_list[i])
        p3=np.divide(y_list[i]-np.divide(M[i]*h_list[i]**2,6),h_list[i])
        p4=np.divide(y_list[i+1]-np.divide(M[i+1]*h_list[i]**2,6),h_list[i])
        s_dict_list.append({'p1':p1,'p2':p2,'p3':p3,'p4':p4,'x1':x_list[i],'x2':x_list[i+1]})
    return section_list,s_dict_list
def main_r(x,section_list,s_list):
    def interpolation_function_r(x,params):
        return params['p1']*((params['x2']-x)**3)+params['p2']*(x-params['x1'])**3+params['p3']*(params['x2']-x)+params['p4']*(x-params['x1'])
    for i in range(len(section_list)):
        if x>=section_list[i][0] and x<=section_list[i][1]:
            return interpolation_function_r(x,s_list[i])
        if x<section_list[0][0] or x>section_list[len(section_list)-1][1]:
            if x<section_list[0][0]:
                return interpolation_function_r(x,s_list[0])
            else:
                return interpolation_function_r(x,s_list[len(section_list)-1])
def main(x,x_list,y_list):
    section_list,s_dict_list=cubic_spline_interpolation(x_list,y_list)
    return main_r(x,section_list,s_dict_list)
