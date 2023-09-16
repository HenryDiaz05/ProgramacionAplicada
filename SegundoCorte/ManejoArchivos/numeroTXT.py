import random
import os
from time import sleep

for i in range(1):
    if os.path.exists("pseudonumero.txt"):
        os.remove("pseudonumero.txt")
        print("Borrando...")
        print("-----------------------------------------------------")
        sleep(1)
    else:
        print("El archivo no existe")
        print("-----------------------------------------------------")

n = int(input("Ingrese la cantidad de numero que desea guardar: "))

for i in range (n):
    num = random.uniform(0,1)
    numr = round(num, 2)
    txt = open("pseudonumero.txt", "a")
    txt.write(str(numr) + '\n')
    txt.close()