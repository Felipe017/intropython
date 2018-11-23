# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:08:06 2018

@author: Lenovo
"""
'---------------------------Bibiliotecas Utilizadas--------------------------'

import matplotlib.pyplot as plt
import math 

'---------------------------Condições iniciais-------------------------------'
 
m = float(input('Massa: '))
k = float(input('Constante elástica: '))
g = 9.81
lo = float(input('comprimento natural: '))
ri = float(input('comprimento inicial: '))
theta = math.radians(float(input('Valor do angulo: ')))
t = float(input('Tempo total contabilizado: ')) 
v_theta = 0
v_r = 0
cont_tempo = 0 

'---------------------------Listas construidas-------------------------------'

x = []
z = []
r = []
thetai = []
tn = []
vr = []
vtheta = []
tn = []

'----------------------------LOOP utilizado-----------------------------------'

while (t >= cont_tempo):
    
    cont_tempo = cont_tempo + 0.001   
    
    a_theta = (-2*v_r*v_theta)/ri - (g/ri)*math.sin(theta)
    v_theta  = v_theta + a_theta*0.001
    theta = theta + v_theta*0.001
   
    a_r =  -(k/m)*(ri-lo) + g*math.cos(theta) + ri*(v_theta)**2
    v_r  = v_r + a_r*0.001
    ri = ri + v_r*0.001
    
    
    x.append(ri*math.sin(theta))
    z.append(-ri*math.cos(theta))
    thetai.append(math.degrees(theta))
    r.append(ri)
    vtheta.append(v_theta)
    vr.append(v_r)
    tn.append(cont_tempo)

'------------------------------Tabelas----------------------------------------'

print(thetai)
print('')
print(r)
print('')
print(vr)
print('')
print(vtheta)
print('')
print(x)
print('')
print(z)
print('')

'------------------------------Gráficos--------------------------------------'
plt.plot(x,z)
#plt.plot(t,z)
    