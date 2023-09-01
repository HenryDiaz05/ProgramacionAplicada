lista = []

def intervalo():
    n = int(input("ingrese el rango de numeros: "))
    primo(n)
    
        
def primo(n):
    a = 2
    primo = True
    while (a < n+1):
        for i in range(2, a):
            if (a % i == 0):
                primo = False
        if (primo):
            anexar(a)
        else:
            primo = True
        a += 1
    
def anexar(a):
    lista.append(a)
    return lista

def main():
    intervalo()
        

if __name__ == '__main__':
    main()
    print(lista)





        
