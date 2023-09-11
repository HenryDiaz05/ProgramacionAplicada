#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()

print(my_lista) #Imprime lista completa
print(type(my_lista)) #Imprime el tipo list o la clase lista
print(my_lista[2])#Imprime el elemento de la posicion 2 (0,1,2) siendo el amarillo que es el tercer elemento

print("my_lista size: ", len(my_lista)) #cantidad de elementos de la lista
#Imprime los elementos de la lista exeptuando el rango superior en este caso el 2 si desea hasta el dos se debe poner [0:3]
print(my_lista[0:2]) 
print(my_lista[:2])

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro') # Anexa a la posicion 3 el color negro y desplaza los otros elementos 1 posicion
print(my_lista)


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)

print(my_lista.index('Azul')) #indica el numero de la posicion en la que se encuentra el objeto


my_lista.remove('Marron') #elimina un elemento de la lista
print(my_lista)

my_lista.insert(8, 'Marron') #inserta en la posicion indicada un elemento
print(my_lista)

print(my_lista.pop()) #muestra el ultimo elemento de la lista
size = len(my_lista) #cantidad de elementos de la lista
print("size = ", size)


my_lista_3 = my_lista*3 #triplica los elemtos de la lista en el mismo orden en el que estaban ej: (1,2,3)*3 =(1,2,3,1,2,3,1,2,3)
print("my_lista_3: ", my_lista_3)

"""
Para este caso la funcion sort solo funciona para numeros y no para cadenas de texto
"""
print("Sort:")
print()
my_listaSort = my_lista.sort()#no mostrara nada
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] 
print("Ordering my_NumList: ")
my_NumList.sort() #ordenara todos los numero de menor a mayor
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
