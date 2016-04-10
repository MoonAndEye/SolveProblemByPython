# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 22:53:32 2016

@author: Moon

平分七筐魚，有甲乙丙三位魚夫一起出海打魚。身上帶了21只籮筐。

當天結束後，七筐滿的，七筐半滿，七筐空的。

假設滿的，半滿的，程度完全相同。

在不倒出任何一條魚的情況，如何將魚和魚筐平分三份?

"""

import numpy as np

def initMatrix(dimension = 1, init = 0):
    matrix = []    
    for i in range(dimension):
        for i in range(dimension):
            pass
    

i = 0

fall = i

half_f = (3.5 - fall) * 2

empty = 7 - fall - half_f

