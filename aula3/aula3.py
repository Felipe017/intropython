# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:36:54 2018

@author: Lenovo
"""

print('Exercicio proposto 01')

print('')

import math 

cateto_oposto = 4
cateto_adjacente = 2
tangente_theta = cateto_oposto/cateto_adjacente
theta=math.atan(tangente_theta)
print(theta, 'em radianos')
theta_graus = math.degrees(theta)
print(theta_graus,'em graus')

print('')

print('Exercicio proposto 02')

print('')

cos = (2**0.5)/2
theta1 = math.acos(cos) 
print(theta1,'em radianos')
theta1_graus = math.degrees(theta1)
print(theta1_graus,'em graus')

print('')

print('Add novas funções')

print('')

def print_poema():
    print('Caminante, no hay camino,')
    print('se hace camino al andar.')
print_poema()

def verso_poema ():
    print('Al andar se hace el camino,')
    print('y al volver la vista atrás,')
    print('se ve la senda que nunca')
    print('se ha de volver a pisar.')
    print('Caminante no hay camino')
    print('sino estelas en la mar.')
verso_poema()

print('')

print('Exercicios Aula 3')
print('')
print('Ex 01')

def chocolate (x):
    print(x)
    print(type(x))
chocolate(verso_poema())

print('')
def print_valor_tipo (x=0):
    #print(x)
    print(type(x))
print_valor_tipo()

print('Ex 02')
print('')

def print_MRU (so,s,t):
    print('espaço final: ',s)
    print('espaço inicial: ',so)
    print('tempo: ',t)
    v=(s-so)/t
    print('velocidade é: ',v, 'm/s')

print_MRU(5,15,2)

print('')
    
print('Ex 03')
print('')

def funcaoZ(h,l):
    tan=h/l
    theta2=math.atan(tan)
    #print(theta2)
    return theta2
alpha = funcaoZ(5,0.5)
print(alpha,'radiano')
print('')

print('Ex 04')

def conv_Milha_metro(M):
    conv_metro = 1.61*10**3*M
    return conv_metro
valor_metro = conv_Milha_metro(1)
print('Valor de uma milha em metros ',valor_metro)

def conv_metro_Milha(m):
    conv_milha = m/(1.61*10**3)
    return conv_milha
valor_milha = conv_metro_Milha(1)
print('Valor de um metro em milhas ',valor_milha)

def conv_mi_km (Mi):
    conv_km = 1.61*Mi
    return conv_km
valor_km = conv_mi_km(1)
print('Valor de uma milha em Km ', valor_km)

def conv_kmetro_metro(metro):
    conv_metro1 = metro*10**3 
    return conv_metro1
valor_metro1= conv_kmetro_metro(1)
print('Valor de um kilometro em metro ',valor_metro1)

def conv_Hrseg(hr):
    seg=3600*hr
    return seg
valor_temp_seg=conv_Hrseg(1)
print('Tempo de uma horas em segundos ',valor_temp_seg)

def conv_segHora(segundos):
    hora=segundos/3600
    return hora
valor_temp_hora=conv_segHora(1)
print('Tempo de um segundos em horas ',valor_temp_hora)

v=4*valor_km/0.5
print('Valor de velocidade em km/hr: ',v)
v1=4*valor_metro/(0.5*valor_temp_seg)
print('Valor da valocidade em m/s',v1)

print('Ex 05')
print('')
print('IMC')
print('')
def imc (f,M,H):
    f(M,H)
def massa (M): 
    m=M
    return m 
valor_massa= massa(float(input('Valor da massa: ')))
print('Valor da massa', valor_massa)

def altura (H):
    h=H
    return h
valor_altura= altura(float(input('Valor da altura: ')))
print('Valor da altura', valor_altura)

IMC= valor_massa/valor_altura**2 
print('Imc é ',IMC)

def raio (R):
    r=R
    return r
valor_raio=raio(float(input('raio: ')))
volume=(4*pi*valor_raio*3)/3
print('Valor do volume da esfera é: ',volume)

print('')
print('Distancia entre pontos')

def y (f,D,d,L):
    f(D,d,L)
def y1 (D,d,L):
    y2=D*L/d
    print(y2)
    return (y2)
y(y1,98,0.250*10**(-3),632.8*10**(-9))
#print(y2)













