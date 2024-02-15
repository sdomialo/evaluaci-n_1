#Ejercicio 1: Extracción de Información de una Receta

#Al extraer texto de un sitio web de recetas, obtuviste una cadena de texto corrupta y al revés. Parece contener el nombre de una receta y la cantidad de calorías. Formatea la cadena para conseguir una estructura como la siguiente:
 
#La receta de [Nombre de la receta] contiene [Número] calorías. 

#Para voltear una cadena rápidamente utilizando slicing: cadena[::-1]

cadena = "etilacorP aicilopoc aroC"
nombre_receta = cadena[::-1]
calorias = 300
formatted_string = "La receta de {} contiene {} calorías.".format(nombre_receta, calorias)
print(formatted_string)
