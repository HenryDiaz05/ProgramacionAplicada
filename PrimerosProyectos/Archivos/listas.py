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



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)