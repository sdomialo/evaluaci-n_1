def separar_personajes(personajes):
    humanos = []
    no_humanos = []
    
    for personaje in personajes:
        if personaje["tipo"] == "humano":
            humanos.append(personaje)
        else:
            no_humanos.append(personaje)
    
    humanos.sort(key=lambda x: x['nombre'])
    no_humanos.sort(key=lambda x: x['nombre'])
    
    return humanos, no_humanos

def agregar_personaje():
    nombre = input("Introduce el nombre del personaje: ")
    tipo = input("¿Es humano? (s/n): ").lower()
    return {"nombre": nombre, "tipo": "humano" if tipo == 's' else "no humano"}

# Ejemplo de uso
personajes = [
    {"nombre": "Mario", "tipo": "humano"},
    {"nombre": "Bob Esponja", "tipo": "no humano"},
    {"nombre": "Link", "tipo": "humano"},
    {"nombre": "Doraemon", "tipo": "no humano"},
    {"nombre": "Master Chief", "tipo": "humano"}
]

while True:
    humanos, no_humanos = separar_personajes(personajes)
    print("Personajes humanos:", humanos)
    print("Personajes no humanos:", no_humanos)

    nuevo_personaje = agregar_personaje()
    personajes.append(nuevo_personaje)
