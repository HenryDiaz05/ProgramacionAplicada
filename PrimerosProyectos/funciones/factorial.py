

def ingreso():
    while True:
        n = int(input("ingrese un numero positivo del factorial que desea obtener: "))
        if (n >0): 
            factorial(n)
        else:
            print("Ingrese un numero positivo")
    

def factorial(n):
    a = 1
    for i in range(1, n+1):
        a = a*i   
    imprimir(a, n)


def imprimir(a, n):
    print(n,"! = ", a)

def main():
    ingreso()
    

if __name__ == '__main__':
    main()

