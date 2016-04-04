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
test = [1,2,2,35]

for each in test:
    a = notRepeat(test)
    print(a)
    b = test.count(each)
    print(b)
"""
                    