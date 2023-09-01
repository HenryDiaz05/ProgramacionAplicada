import random
from matplotlib import pyplot as plt

numbers_a = range(1, 13)
#generamos numeros random enteros entre 1 y 200 para b
numbers_b = [random.randint(1, 29) for i in range(12)] 
# asiganmos un numero aleatorio para cada numero de a en un plano cartesiano
plt.plot(numbers_a, numbers_b)
plt.show()#mostramos la tabla