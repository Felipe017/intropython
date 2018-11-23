#import matplotlib.pyplot as plt
#min=(1/60)horas
#t=5/12 
#t=0.416666666666666  tempo em horas 
#t=25 minutos
print('Ex01')
t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 

print(t)


print('')

def mru (n):

	vo= 0.2 # 12 km/h , 0.2 km/min
	x=[]
	d=0
	i=0
	while i<=n:
		i=i+1
		d = d + vo*1
		x.append(d)
	return x

print(mru(24))

print('Ex02')
