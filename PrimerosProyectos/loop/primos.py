lista = []
n = int(input("ingrese el rango de numeros: "))
a = 2
primo = True
while (a < n+1):
    for i in range(2, a):
        if (a % i == 0):
            primo = False
    if (primo):
        lista.append(a)
    else:
        primo = True
    a += 1

print(lista)