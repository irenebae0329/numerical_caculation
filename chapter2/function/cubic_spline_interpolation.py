#三次样条插值
import sympy 
import numpy as np
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
        if i==0 or i==degree:
            return 0
        else:
            return 6*(equal_difference_n(i-1)-equal_difference_n(i))/(h_list[i-1]+h_list[i])
    def caculate_attr(x_list,y_list,h_list):
        d_list=[]
        for i in range(degree+1):
            mat[i][i]=2
            d_list.append(d(i))
            if i>=1 and i<=degree-1:
                mat[i][i-1],mat[i][i+1]=h_list[i-1]/(h_list[i-1]+h_list[i]),h_list[i]/(h_list[i]+h_list[i-1])
        return np.linalg.inv(mat)@d_list
    
    section_list,h_list=create_section_list(x_list)
    M=caculate_attr(x_list,y_list,h_list)
    s_list=[]
    for i in range(len(section_list)):
        s_list.append(lambda x:M[i]*pow((x_list[i+1]-x),3)/6*h_list[i]+M[i+1]*pow((x-x_list[i]),3)/6*h_list[i]+(y_list[i]-M[i]*pow(h_list[i],2)/6)*(x_list[i+1]-x)/h_list[i]+(y_list[i+1]-M[i+1]*pow(h_list[i],2)/6)*(x-x_list[i])/h_list[i])
    return section_list,s_list
def interpolation_function(x,section_list,s_list):
    for i in range(len(section_list)):
        if x>=section_list[i][0] and x<section_list[i][1] or x==section_list[len(section_list)-1][1]:
            return s_list[i](x)
        else:
            if x<section_list[0][0]:
                return s_list[0](x)
            else:
                return s_list[len(section_list)-1](x)
def main(x,x_list,y_list):
    section_list,s_list=cubic_spline_interpolation(x_list,y_list)
    return interpolation_function(x,section_list,s_list)
#print(main(27.8))
print(main(1.1,[0.2,0.4,0.6,0.8,1.0],[0.98,0.92,0.81,0.64,0.38]))