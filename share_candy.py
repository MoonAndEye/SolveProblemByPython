# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:53:58 2016

@author: Moon

分糖果，老師分給
1 > 10個
2 > 2個
3 > 8個
4 > 22個
5 > 16個
6 > 4個
7 > 10個
8 > 6個
9 > 14個
10 > 20個

所有小孩將自已的糖果分給右邊一半
糖果數為奇數的，可以多向老師要一個
問
要經過幾次，大家的糖果才一樣?
然後又是幾顆?

"""
a = [i*2 for i in range(5)]
b = [i*2-1 for i in range(1,6)]

c = [a+b for a, b in zip(a,b)]
print(a)
