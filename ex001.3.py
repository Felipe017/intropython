# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 09:42:56 2018

@author: Felipe Aguiar
"""
print('Programa para calcular valores de raiz')
print('y = ax^2 + bx + c = 0')

a=float(input('Digite o valor do coeficiente a '))
b=float(input('Digite o valor do coeficiente b '))
c=float(input('Digite o valor do coeficiente c '))
delta=b**2-4*a*c
print(delta)
x1= (-b + (delta)**0.5)/(2*a)
x2= (-b - (b**2-4*a*c)**0.5)/(2*a)
 
print('valo das raizes')
print(x1)
print(x2)
print('fim')
        