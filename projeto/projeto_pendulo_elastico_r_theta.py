print('Simulador de Pendulo Elástico Simples')
print('Autores: Felipe Aguiar e Lucas Conceição')
print('Agradecimento especial Gustavo Borges')

'---------------------------Bibiliotecas Utilizadas--------------------------'

import matplotlib.pyplot as plt
import math 

'---------------------------Condições Iniciais-------------------------------'
print('Condições Iniciais')
print('OBS: É aconselhavel utilizar valores próximos a escala real') 
m = float(input('Massa (kg): '))
k = float(input('Constante elástica (N*m^-1): '))
g = 9.81
lo = float(input('Comprimento natural (m): '))
ri = float(input('Comprimento inicial (m): '))
thetai = math.radians(float(input('Angulo inicial (graus): ')))
t = float(input('Tempo total contabilizado (s): ')) 
v_theta = 0 #Velocidade inicial em theta
v_r = 0 #Velocidade inicial em r
cont_tempo = 0 # contador de tempo
delta_tempo = 0.001 # delta tempo, quanto menor for, maior a precisão do programa

'---------------------------Listas construidas-------------------------------'

x = [] #lista com os valores da posição em relação ao eixo x
z = [] #lista com os valores da posição em relação ao eixo z
r = [] #lista com os valores da posição em relação a coordenada r (polar)
theta = [] #lista com os valores da posição em relação a coordenada theta (polar)
tn = [] # lista do tempo contabilizando cada instante
vr = [] # lista da velocidade em relação a coordenada r, contabilizando cada instante
vtheta = [] # lista da velocidade em relação a coordenada , contabilizando cada instante
energia = [] # lista da energia mecãnica
v = [] # lista da velocidade em módulo
a = [] # aceleração em módulo

'----------------------------LOOP utilizado-----------------------------------'

while (t >= cont_tempo): # Enquanto t for maior ou igual a variavel contador, essa variavel vai crescendo somando-se um delta_tempo
   
    cont_tempo = cont_tempo + delta_tempo  

# Calculando a lagrangeana obtemos a EDO de segunda ordem, isolando as acelerações das coordenadas generalizadas, obtemos a seguinte relação:

    a_theta = (-2*v_r*v_theta)/ri - (g/ri)*math.sin(thetai) # aceleração em theta
    v_theta  = v_theta + a_theta*delta_tempo    # Sabemos também que velocidade = velocidade inicial + aceleração*tempo
    thetai = thetai + v_theta*delta_tempo # De forma análoga calculamos a posição
   
    a_r =  -(k/m)*(ri-lo) + g*math.cos(thetai) + ri*(v_theta)**2 # aceleração em r
    v_r  = v_r + a_r*delta_tempo
    ri = ri + v_r*delta_tempo

    v_t = (v_r**2 + (ri*v_theta)**2)**0.5 		# velocidade resultante 
    ai =  (a_r**2 + a_theta**2)**0.5			# aceleração resultante
    en = (m*v_t**2)/2 - m*g*ri*math.cos(thetai) + (k*(ri-lo)**2)/2	# energia mecânica 
# Por conta do LOOP, podemos preencher cada uma das listas usando a função .append
    x.append(ri*math.sin(thetai))
    z.append(-ri*math.cos(thetai))
    theta.append(math.degrees(thetai))
    r.append(ri)
    vtheta.append(v_theta)
    vr.append(v_r)
    tn.append(cont_tempo)
    v.append(v_t)
    a.append(ai)	
    energia.append(en)

'------------------------------Dados obtidos---------------------------------'
#Para criar uma arquivo txt foi utilizado a função "open"
#Função para replicar a criação para varias possibilidades  
def tabela(nome,lista):
    lista = str(lista)
    arquivo = open(nome + '.txt', 'a')
    arquivo.write(lista + '\n')
    arquivo.close

tabela('Lista Temporal', tn)
tabela('Lista da posição do eixo x', x)
tabela('Lista da posição do eixo z', z)
tabela('Lista da velocidade', v)
tabela('Lista da aceleração', a)
tabela('Lista da posição na coordenada r, polar', r)
tabela('Lista da posição na coordenada theta(angulo)', theta)
tabela('Lista da velocidade coord. r',vr)
tabela('Lista da velocidade coord. theta', vtheta)
tabela('Lista da energia mecânica', energia)

'------------------------------Gráficos--------------------------------------'
#Para criar os gráficos usamos o plt.plot, veja melhor as funçõe do "plt"
#Função para replicar a criação para varias possibilidades         
def grafico(x,y,nome_eixo_x,nome_eixo_y):
    plt.plot(x,y)
    plt.xlabel(nome_eixo_x)
    plt.ylabel(nome_eixo_y)
    plt.show()

grafico(tn,theta,'tempo(s)', 'angulo (graus)')
grafico(tn,r,'tempo(s)', 'r (m)')
grafico(r,theta,'r(m))', 'angulo (graus)')
grafico(tn,z,'tempo(s)', 'eixo z (m)')
grafico(tn,x,'tempo(s)', 'eixo x (m)')
grafico(x,z,'eixo x (m)', 'eixo z (m)')
grafico(tn,v,'tempo(s)', 'velocidade (m.s*-1)')
grafico(tn,a,'tempo(s)', 'aceleração (m.s*-2)')
grafico(tn,energia,'tempo(s)', 'Energia (J)') # A energia mecânica deve se conservar, porém o programa mostra uma variação da energia, essa variação é por conta do erro do programa, para diminuir a variação deve aumentar o valor do delta_tempo
print('A energia mecânica deve se conservar, porém o programa mostra uma variação da energia, essa variação é por conta do erro do programa, para diminuir a variação deve aumentar o valor do delta_tempo')

