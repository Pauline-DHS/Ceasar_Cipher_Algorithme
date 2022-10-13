import random
import time

Password = str(random.randint(0,9999999))

start = time.time()

for i in range(10000000):
	Trial = str(i) #str converti n'importe quelle variable en chaine
	if Trial == Password:
		print('Found password : ' + Password)
		break

end = time.time()

print('Found in '+format(end-start)+' sec')
