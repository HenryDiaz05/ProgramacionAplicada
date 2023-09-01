a = input("Ingrese el numero a: ")
a = int(a)
b = input("Ingrese el numero b: ")
b = float(b)
c = a + b

if a == b:
    print("igual")
else:
    print("diferente")

print("el tipo de a es: ", type(a))
print("el tipo de b es: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a y b tienen el mismo tipo")
else:
    print("a y b tiene diferente tipo")