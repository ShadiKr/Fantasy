# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:46:09 2018

@author: Shadi Kreidly
"""

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))

yi = y - (14 - m)//12
x = yi + yi//4 - yi//100 + yi//400
mi = m + 12 * ((14 - m)//12) - 2
di = (d + x + (31 * mi)//12) %7

print(di)