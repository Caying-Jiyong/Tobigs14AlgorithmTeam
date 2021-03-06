# -*- coding: utf-8 -*-
"""5주차_동적계획법_주원1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1at3v7R4S3nGyGTGoeLvyMMPSwkRaxx8f
"""

N = int(input())
dr = 0
dg = 0
db = 0

for i in range(N):
    r, g, b = [ int(x) for x in input().split() ]
    r += min(dg, db)
    g += min(dr, db)
    b += min(dr, dg)
    dr, dg, db = r, g, b
    
print(min(dr, dg, db))