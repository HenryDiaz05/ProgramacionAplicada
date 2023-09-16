#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']


print("############TUPLAS#########")
my_tupla = tuple(my_lista)#convertimos la lista en una tupla
print()
print()
print("my_tuple: ", my_tupla)

#Imprimira el dato que se encuentra en la posicion indicada de la tupla
print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print('negro' in my_tupla) #indicara que no esta en la lista como false
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

#ejemplo

tuplaEj = "Desayuno", "almuerzo", "cena"
comida1, comida2, comida3 = tuplaEj

print(comida1)
print(comida2)
print(comida3)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)