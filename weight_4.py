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

for w1 in range(1,40):
    for w2 in range(1,40):
        for w3 in range(1,40):
            for w4 in range(1,40):
                if w1 + w2 + w3 +w4 == 40:
                    temp=[]
                    temp=[w1, w2, w3,w4]
                    temp.sort()
                    sol_space.append(temp)
                    
print(sol_space)
                    