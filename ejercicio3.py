#Ejercicio 3: Encontrar Palabras Comunes

#Dadas dos listas de palabras, genera una tercera lista con todas las palabras que se repitan en ambas listas, sin repetición en la nueva lista.

list1 = ["mono", "tortuga", "gato", "oso"]
list2 = ["tortuga", "gato", "oso", "sopa"]

common_words = list(set(list1) & set(list2))
print(common_words)