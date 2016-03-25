# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:55:03 2016

@author:
"""
income = input("Enter your salary: ")

#tax range 放的是稅率的邊界
taxrange = [0,500,2000,5000,20000,40000,60000,80000,100000]

rate = [5,10,15,20,25,30,35,40,45]

basic_level = 3500
#這一行可以改，如果低於這個數字，就不用繳稅，也是扣除額


def find_tax_level(salary = 0, taxrange= list):
    tax_level = 0
    salary = int(salary)
    for i in range(len(taxrange)):
        if salary > taxrange[i] and salary < taxrange[i+1]:
            tax_level = i
        else:
            pass
    return (tax_level)

def tax_judgement(income = 0):
    income = int(income)
    if income <= basic_level:
        print("You don't need to pay tax")
    else:
        tax_level = find_tax_level(income, taxrange)
        tax_rate = rate[tax_level]        
        pay_tax = 625 + (income - basic_level)*tax_rate/100
        print("You need to pay " + str(pay_tax))     
tax_judgement(income)
# Death and Tax, they are certain.
