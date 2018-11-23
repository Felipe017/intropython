# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:26:26 2018

@author: Lenovo
"""

import matplotlib.pyplot as plt
import math 

pi = math.pi 
m = float(input('Massa: '))
k = float(input('Constante elástica: '))
g = 9.81
lo = float(input('comprimento natural: '))
r = float(input('comprimento inicial: '))
theta = math.radians(float(input('Valor do angulo: ')))
t = float(input('Valor do tempo: '))
xi = math.sin(theta)*r
zi = math.cos(theta)*r

x = []
z = []

tn = []

vx = []
vz = []

vox = 0
voz = 0

tn = []
a = []
cont_tempo = 0
print(xi)
while (t >= cont_tempo):
    
    cont_tempo = cont_tempo + 0.001   
    
    ax = (k/m)*(r-lo)*math.sin(theta)
    vox  = vox + ax*0.001
    xi = xi + vox*0.001
   
    az =  g - (k/m)*(r-lo)*math.cos(theta)
    voz  = voz + az*0.001
    zi = zi + voz*0.001

    r = (xi**2 + zi**2)**0.5 
    theta = math.atan2(xi,zi)

    x.append(xi)
    z.append(zi)
    vx.append(vox)
    vz.append(voz)
    tn.append(cont_tempo)

print(x)
#print(z)
#print(vx)
#print(vz)

plt.plot(tn,x)
#plt.plot(t,z)
    