# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:09:33 2018

@author: Lenovo
"""

print('Programa que calcula a velocidade e o tempo de um objeto em queda livre, desprezando o atrito')
h=float(input('Digite a altura: '))
g=9.81
v=(2*g*h)**0.5
print('Sua velocidade final será: ',v)
t=v/g
print('o tempo será: ',t)
print('Fim')