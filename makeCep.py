import random

l = list(range(1, 100))
with open('cep.dat', 'w') as arq:
	while len(l) != 0:
		aux = random.choice(l)
		l.remove(aux)
		if aux//10 == 0 : aux = '0'+ str(aux)
		aux = str(aux)
		arq.write(aux)
