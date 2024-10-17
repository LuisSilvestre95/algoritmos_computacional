class Nodo:
    def __init__(self, estado, padre=None, costo=0, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo
        self.profundidad = profundidad

    def __lt__(self, otro):
        return self.costo < otro.costo

def busqueda_en_haz(inicio, objetivo, generar_vecinos, ancho_haz, profundidad_maxima=10):
    haz = [Nodo(inicio)]
    
    while haz:
        siguiente_haz = []
        
        for nodo in haz:
            print(f'Explorando nodo: {nodo.estado} con costo: {nodo.costo} y profundidad: {nodo.profundidad}')  # Mensaje de depuración
            if nodo.estado == objetivo:
                return reconstruir_camino(nodo)

            if nodo.profundidad < profundidad_maxima:
                vecinos = generar_vecinos(nodo)
                siguiente_haz.extend(vecinos)

        if not siguiente_haz:
            print("No se generaron vecinos en esta iteración.")
        
        # Ordenar y seleccionar los mejores nodos
        siguiente_haz = sorted(siguiente_haz)[:ancho_haz]
        haz = siguiente_haz

    return None  # No se encontró la solución

def generar_vecinos(nodo):
    # Ejemplo simple de generación de vecinos
    vecinos = []
    for i in range(1, 4):  # Supongamos que podemos generar hasta 3 vecinos
        nuevo_estado = f'{nodo.estado}-{i}'
        vecinos.append(Nodo(nuevo_estado, nodo, nodo.costo + 1, nodo.profundidad + 1))
    return vecinos

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return camino[::-1]  # Invertir el camino

# Ejemplo de uso
if __name__ == "__main__":
    inicio = 'A'
    objetivo = 'A-3'  # Objetivo
    ancho_haz = 5  # Aumentar el ancho del haz
    profundidad_maxima = 10  # Aumentar la profundidad máxima
    camino = busqueda_en_haz(inicio, objetivo, generar_vecinos, ancho_haz, profundidad_maxima)
    if camino:
        print(f'Ruta encontrada: {camino}')
    else:
        print('No se encontró una ruta.')
        