# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:08:09 2018

@author: Lenovo
"""
print('Programa de IMC')
m=float(input('Peso: '))
a=float(input('Altura: '))
imc= m/a**2
print('Seu IMC é: ', imc)
if (imc>25):
    print('Você está acima do Peso')
elif (imc<20):
    print('Você está abaixo do Peso')
    if ( 20 < imc > 25):
        print('Você está no peso ideal')
    elif (imc):
            print('Fim')