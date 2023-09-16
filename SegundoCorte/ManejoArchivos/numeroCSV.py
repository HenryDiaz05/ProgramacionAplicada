import random
import csv
import os


try:
    os.remove("pseudonumero.csv")
except OSError:
    print("No se pudo borrar el archivo")


n = int(input("Ingrese la cantidad de numero que desea guardar: "))

list = []
for i in range (n):
        num = random.uniform(0,1)
        numr = round(num, 2)
        list.append(numr)
    

with open('pseudonumero.csv', 'a') as a:
    numero = csv.writer(a)
    numero.writerow(list)
    a.close()
    