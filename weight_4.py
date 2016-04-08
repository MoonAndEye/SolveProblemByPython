# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:49:40 2016
@author: Moon
"""

w1 = 0
w2 = 0
w3 = 0
w4 = 0
sol_space = []

def notRepeat(in_list = list):
    copy_list = in_list
    check_list = []
    for each in in_list:
        check = 0
        if int(copy_list.count(each)) <2:
            check = 0
            check_list.append(check)
        else:
            check = 1
            check_list.append(check)
    return(sum(check_list))

def delRepeat(in_list = list):
    temp = []
    
    for each in in_list:
        if each not in temp:
            temp.append(each)
    return(temp)

for w1 in range(1,40):
    for w2 in range(1,40):
        for w3 in range(1,40):
            for w4 in range(1,40):
                if w1 + w2 + w3 +w4 == 40:
                    temp=[]
                    temp=[w1, w2, w3,w4]
                    temp.sort()
                    if notRepeat(temp) == 0:
                        sol_space.append(temp)
                    
real_sol_space = delRepeat(sol_space)                   
#print(sol_space)
"""
def exhuastive(sol_s=list, coefficient=list, fit=list):
"""            
    #sol_s 這邊放解空間

    #這邊放係數

    #這邊放解答
"""
    return_list=[]
    for each_s in sol_s:
        index = 0
        for try_fit in fit:
            for a1 in coefficient:
                for a2 in coefficient:
                    for a3 in coefficient:
                        for a4 in coefficient:
                            if a1*each_s[0] +a2*each_s[1] +a3*each_s[2] +a4*each_s[3] - try_fit == 0:
                                index = index +1
                            else:
                                pass
        if index == 40:
            return_list.append(each_s)
                
    return(return_list)        
"""        
a = [i for i in range(1,41)]
#b = exhuastive(sol_space, [-1,0,1],a)
#print(b)
answer = []
for weight in real_sol_space:
    solve = {}
    x1 = weight[0]
    x2 = weight[1]
    x3 = weight[2]
    x4 = weight[3]
    for tryFit in range(1,41):
        for a1 in range(-1,2):
            for a2 in range(-1,2):
                for a3 in range(-1,2):
                    for a4 in range(-1,2):
                        if a1 * x1 + a2 * x2 + a3 * x3 + a4 * x4 == tryFit:
                            solve[tryFit] = [a1,a2,a3,a4]
                            
                        else:
                            pass
                    
    if len(solve) == 40:
        answer.append(weight)
    else:
        pass
        
print("四個砝碼質量分別是" + str(answer[0])+'\n' )              
print("下面是秤出1到40克的組合方式")
answer = answer[0]
p1 = answer[0]
p2 = answer[1] 
p3 = answer[2]
p4 = answer[3]

for tryFit in range(1,41):
    for a1 in range(-1,2):
        for a2 in range(-1,2):
            for a3 in range(-1,2):
                for a4 in range(-1,2):
                    if a1 * p1 + a2 * p2 + a3 * p3 + a4 * p4 == tryFit:
                        multi = " * "
                        plus = " + "
                        
                        a1p = str(a1)
                        a2p = str(a2)
                        a3p = str(a3)
                        a4p = str(a4)
                        p1p = str(p1)
                        p2p = str(p2)
                        p3p = str(p3)
                        p4p = str(p4)
                        
                        printout = a1p + multi + p1p + plus + a2p + multi +p2p + plus +a3p+ multi +p3p + plus + a4p + multi +p4p
                        print( str(tryFit) + " = " + printout)
