import heapq

class Nodo:
    def __init__(self, nombre, padre=None, g=0, h=0):
        self.nombre = nombre
        self.padre = padre  # Nodo padre
        self.g = g  # Costo desde el inicio hasta el nodo
        self.h = h  # Costo estimado desde el nodo hasta el objetivo
        self.f = g + h  # Costo total

    def __lt__(self, otro):
        return self.f < otro.f

def a_estrella(inicio, objetivo, grafo, heuristica):
    lista_abierta = []
    conjunto_cerrado = set()

    nodo_inicio = Nodo(inicio, None, 0, heuristica[inicio])
    heapq.heappush(lista_abierta, nodo_inicio)

    while lista_abierta:
        nodo_actual = heapq.heappop(lista_abierta)
        if nodo_actual.nombre == objetivo:
            return reconstruir_camino(nodo_actual)

        conjunto_cerrado.add(nodo_actual.nombre)

        for vecino, costo in grafo[nodo_actual.nombre].items():
            if vecino in conjunto_cerrado:
                continue
            g_score = nodo_actual.g + costo
            h_score = heuristica[vecino]
            nodo_vecino = Nodo(vecino, nodo_actual, g_score, h_score)

            if nodo_vecino in lista_abierta:
                continue

            heapq.heappush(lista_abierta, nodo_vecino)

    return None  # No se encontró una ruta

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.nombre)
        nodo = nodo.padre
    return camino[::-1]  # Invertir el camino

# Ejemplo de uso
grafo = {
    'Parque': {'Cafetería': 2, 'Biblioteca': 5},
    'Cafetería': {'Parque': 2, 'Museo': 4, 'Biblioteca': 1},
    'Biblioteca': {'Parque': 5, 'Cafetería': 1, 'Museo': 3},
    'Museo': {'Cafetería': 4, 'Biblioteca': 3}
}

heuristica = {
    'Parque': 6,
    'Cafetería': 4,
    'Biblioteca': 2,
    'Museo': 0
}

inicio = 'Parque'
objetivo = 'Museo'
camino = a_estrella(inicio, objetivo, grafo, heuristica)
print(f'Ruta más corta: {camino}')