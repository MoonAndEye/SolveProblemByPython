# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:29:37 2016

@author: 

零存整付的概念

小明的爸要準備小明的生活費

假設一個月小明拿出 x = 1000 金
而假設銀行率 y = 1.71 %
小明有n = 4 年要過
一開始要存多少
用字典
"""

withdraw = 1000
interest = 1.71
# 這邊假設利率都是年利，而且不讓使用者需要轉換
interest = interest/100
monthes = 48

deposit = 0

detail = []
interest_detail = [(1 + interest/12)**x for x in range(monthes)]
for i in range(monthes):
    monthes_index = 48 - i
    this_month_depo = withdraw/interest_detail[i]
    if i == 0:
        detail.append(this_month_depo)
    else:
        deposit = this_month_depo + detail[i-1] 
        detail.append(deposit)
    print("第%d個月，你要存%.2f元" % (monthes_index,detail[i]))
