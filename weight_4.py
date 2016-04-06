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

def exhuastive(sol_s=list, coefficient=list, fit=list):
    """            
    sol_s 這邊放解空間

    這邊放係數

    這邊放解答
    """
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
        print(each_s)        
        print(index)
        
a = [i for i in range(1,41)]
exhuastive(sol_space, [-1,0,1],a)
