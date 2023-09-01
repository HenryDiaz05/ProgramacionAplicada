import time

cadena = 'Python kttkktktk'

for letra in cadena: # imprime letra por letra de la string
   if letra == 't':# evita que se escriba la letra indicada 
      continue
   print(letra)
   time.sleep(1) #tiempo de espera 1 seg
   