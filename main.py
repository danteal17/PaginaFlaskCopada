

import random

azar = random.randrange(0,7)

# texto == string
# numero = int / float


azar =  str(azar)


#nombre
with open(azar + ".txt","w") as archivo:
    #contenido
    archivo.write(azar)


input()


