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
children = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
a = [i*2 for i in range(5)]
b = [i*2-1 for i in range(1,6)]

c = [a+b for a, b in zip(a,b)]
#print(a)
d = [int(i/2) for i in a]


#print(d)

def oddPlusOne(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
        else:
            i = i + 1
            new_list.append(i)
    return(new_list)
    
test = oddPlusOne(children)

e = sum(children)/len(children)
f = len(children)

def avgList(list):
    avg = sum(list)/len(list)
    return(avg)

def notEnd(list):
    avg = avgList(list)
    index = 0
    for i in list:
        if i == avg:
            pass
        else:
            index = index + 1
    return(index)

def candyNumGive(list):
    give = oddPlusOne(list)
    last = give.pop(len(give) - 1)
    give.insert(0,last)
    give = [int(i/2) for i in give]
    return(give)
    

#temp = [children-give_to for children, give_to in zip(children, give_to)]
times = 0
while notEnd(children) != 0:
    times = times + 1
    children = oddPlusOne(children)
    
    receive = candyNumGive(children)
    children = [int(i/2) for i in children]
    children = [children + receive for children, receive in zip(children, receive)]
    print("次數: " + str(times) + " 過程: " + str(children) )
print('times is ' + str(times))

print("Result is " + str(children))