#Ejercicio 4: Priorización de Tareas en un Videojuego

#Durante la planificación de un videojuego, se han acordado una serie de misiones con niveles de dificultad. Crea una estructura de cola con todas las misiones ordenadas por dificultad pero sin mostrar los números de dificultad.

from queue import PriorityQueue

# Crear una cola vacía
cola_misiones = PriorityQueue()

# Agregar las misiones a la cola en el orden deseado
cola_misiones.put("Misión fácil")
cola_misiones.put("Misión intermedia")
cola_misiones.put("Misión difícil")

# Mostrar las misiones en el orden de prioridad
while not cola_misiones.empty():
    mision = cola_misiones.get()
    print(mision)
#Durante la planificación de un videojuego, se han acordado una serie de misiones con niveles de dificultad. Crea una estructura de cola con todas las misiones ordenadas por dificultad pero sin mostrar los números de dificultad.
# Create a priority queue
missions_queue = PriorityQueue()

# Add missions to the queue with their difficulty level
missions_queue.put((10, "Mission 1"))
missions_queue.put((7, "Mission 2"))
missions_queue.put((15, "Mission 3"))
missions_queue.put((8, "Mission 4"))
missions_queue.put((25, "Mission 5"))

# Print the missions in order of difficulty
while not missions_queue.empty():
    _, mission = missions_queue.get()
    print(mission)
