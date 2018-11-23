print('Simulador de Pendulo Simples')
print('Autores: Felipe Aguiar e Lucas Conceição')

'---------------------------Bibiliotecas Utilizadas--------------------------'

import matplotlib.pyplot as plt
import math 

'---------------------------Condições Iniciais-------------------------------'
print('Condições Iniciais')
print('OBS: É aconselhavel utilizar valores próximos a escala real') 
m = float(input('Massa (kg): '))
g = 9.81
ri = float(input('Comprimento (m): '))
thetai = math.radians(float(input('Angulo inicial (graus): ')))
t = float(input('Tempo total contabilizado (s): ')) 
v_theta = 0 #Velocidade inicial em theta
cont_tempo = 0 # contador de tempo
delta_tempo = 0.001 # delta tempo, quanto menor for, maior a precisão do programa

'---------------------------Listas construidas-------------------------------'

x = [] #lista com os valores da posição em relação ao eixo x
z = [] #lista com os valores da posição em relação ao eixo z
theta = [] #lista com os valores da posição em relação a coordenada theta (polar)
tn = [] # lista do tempo contabilizando cada instante
vtheta = [] # lista da velocidade em relação a coordenada , contabilizando cada instante
energia = [] # lista da energia mecãnica
a = [] # aceleração 
'----------------------------LOOP utilizado-----------------------------------'

while (t >= cont_tempo): # Enquanto t for maior ou igual a variavel contador, essa variavel vai crescendo somando-se um delta_tempo
   
    cont_tempo = cont_tempo + delta_tempo  

# Calculando a lagrangeana obtemos a EDO de segunda ordem, isolando a aceleração da coordenada generalizada, obtemos a seguinte relação:

    a_theta = - (g/ri)*math.sin(thetai) # aceleração em theta
    v_theta  = v_theta + a_theta*delta_tempo    # Sabemos também que velocidade = velocidade inicial + aceleração*tempo
    thetai = thetai + v_theta*delta_tempo # De forma análoga calculamos a posição
   
    en = (m*v_theta**2)/2 - m*g*ri*math.cos(thetai)	# energia mecânica 
# Por conta do LOOP, podemos preencher cada uma das listas usando a função .append
    x.append(ri*math.sin(thetai))
    z.append(-ri*math.cos(thetai))
    theta.append(math.degrees(thetai))
    vtheta.append(v_theta)
    tn.append(cont_tempo)
    a.append(a_theta)	
    energia.append(en)

'------------------------------Dados obtidos---------------------------------'
#Para criar uma arquivo txt foi utilizado a função "open"
#Função para replicar a criação para varias possibilidades  
def tabela(nome,lista):
    arquivo = open(nome + '.txt', 'a')    
    for j in range(len(lista)):
        lista = str(lista)
        arquivo.write(lista[j] + '\n')
    arquivo.close

tabela('Lista Temporal (P. Simples)', tn)
tabela('Lista da posição do eixo x (P. Simples)', x)
tabela('Lista da posição do eixo z (P. Simples)', z)
tabela('Lista da aceleração (P. Simples)', a)
tabela('Lista da posição na coordenada theta(angulo) (P. Simples)', theta)
tabela('Lista da velocidade coord. theta (P. Simples)', vtheta)
tabela('Lista da energia mecânica (P. Simples)', energia)

'------------------------------Gráficos--------------------------------------'
#Para criar os gráficos usamos o plt.plot, veja melhor as funçõe do "plt"
#Função para replicar a criação para varias possibilidades         
def grafico(x,y,nome_eixo_x,nome_eixo_y):
    plt.plot(x,y)
    plt.xlabel(nome_eixo_x)
    plt.ylabel(nome_eixo_y)
    plt.show()

grafico(tn,theta,'tempo(s)', 'angulo (graus)')
grafico(tn,z,'tempo(s)', 'eixo z (m)')
grafico(tn,x,'tempo(s)', 'eixo x (m)')
grafico(x,z,'eixo x (m)', 'eixo z (m)')
grafico(tn,vtheta,'tempo(s)', 'velocidade angular (rad.s*-1)')
grafico(tn,a,'tempo(s)', 'aceleração angular (rad.s*-2)')
grafico(tn,energia,'tempo(s)', 'Energia (J)') # Energia mecânica se conservar
