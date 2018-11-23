# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:19:49 2018

@author: Lenovo
"""

import math
a = math.exp(0)-math.exp(-10)

x=range(0,10)
y=[math.exp(-xi) for xi in x]  # isto se chama "list comprehension"
print(x)
print(y)

import matplotlib.pyplot as plt
plt.bar(x,y,color="red",align="edge",width=1)
x1=[i/1000 for i in range(0,10000)]
y1=[math.exp(-xi) for xi in x1]
plt.plot(x1,y1)

z1=[]

S = 0
for xi in x:
    S = S+ math.exp(-xi) # *dx que e 1 nesse caso
     
print("Soma 10 caixinhas= ",S)

S1= 0
for xi in x1:
    S1 = S1+ math.exp(-xi) * 0.001
    z1.append(S1)
print("Soma 1000 caixinhas = ",S1)
plt.plot(x1,z1)


r= ((S1 - a)/a)*100 
print(r)


