# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:50:20 2016

@author:

輸入10筆評審的評分資料，砍掉最高，砍掉最低，再取平均
"""

judge_score = []
times = 0
while times != 10:
    score = input("Plz ente " + str(times+1) + " judge's score: " )
    score = float(score)
    times = times + 1
    judge_score.append(score)

judge_score.sort
judge_score = judge_score[1:-1]

average = float(sum(judge_score))/int(len(judge_score))

print(average)
