# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:35:04 2016

@author: Moon

有一車禍發生在某個城市的十字路口

目擊者 a b c  三人

a 說，該車牌前兩個號碼一樣

b 說，該車牌後兩個號碼一樣

c 說，該車牌是某個數的平方

問，該車牌有幾種可能?
"""

"""
以下是想法

1000的平方根是30左右

9999的平方根是100左右

所以設定一個loop，讓 i 從30跑到100，對每個位數取出四位，abcd，

a == b
且 
c == d
那個 i 就是答案

"""

def takeEachDig(number):
    """
    這個回傳的list，
    """
    percentile = []
    percentile = list(number)
    percentile.reverse()
    return(percentile)

test = input("test input: ")

a = takeEachDig(test)

print(a)    
        
