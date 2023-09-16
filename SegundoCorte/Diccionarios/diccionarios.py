sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

#numeros como key o elemento 
numeros = {1:2,3.4:4}
print(numeros)
      
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

print(students_in_classes)

#ingresa a la lista cada letra de la string
students_in_classes["cartography"] += "remi"
print(students_in_classes)

diccionario_vacio = {}
print(diccionario_vacio)

# agregar un nuevo elemento al diccionario
diccionario_vacio["Reptiles"] = 1 
print(diccionario_vacio)

diccionario_vacio["Mamiferos "] = 7 
print(diccionario_vacio)

#sobre-escribe el diccionario
diccionario_vacio = {"Reptiles":1}
print(diccionario_vacio)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
#la funcion update agrega varios elementos y los adjunta al final del diccionario
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"})
#cambia el valor del elemento o key indicada en los parentesis
oscar_winners["Best Picture"] = "Moonlight" 
print(oscar_winners)

#listas con los datos de los diccionarios 1. elementos 2. valores
cafe = ["expresso", "expresso_doble", "Americano"]
cafeina = [50, 100, 25]
#comprimimos ambas cadenas
zipped_cafe = zip(cafe, cafeina)
#agregamos los datos del  comprimido en el diccionario en el orden del comprimido
cafetera = {key:value for key, value in zipped_cafe}
print(cafetera)

#dependiendo del orden en el comprimido cambia la asignacion de los datos en el diccionario
zipped_cafe2 = zip(cafeina, cafe)
cafetera = {key:value for key, value in zipped_cafe2}
print(cafetera)
