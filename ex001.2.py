# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:34:48 2018

@author: Lenovo
"""

v_som = 343 
c= 3*10**8
ts=3
s=v_som*(ts-(v_som*ts)/c)
print('O espaço total é: ',s)
ds= s-v_som*ts
print('A diferença é: ', ds)