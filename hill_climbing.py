import random

def escalada_colina(solucion_inicial, evaluar, generar_vecinos):
    solucion_actual = solucion_inicial
    puntaje_actual = evaluar(solucion_actual)

    while True:
        vecinos = generar_vecinos(solucion_actual)
        mejor_vecino = None
        mejor_puntaje = puntaje_actual

        for vecino in vecinos:
            puntaje = evaluar(vecino)
            if puntaje > mejor_puntaje:  # Suponiendo que más alto es mejor
                mejor_puntaje = puntaje
                mejor_vecino = vecino

        if mejor_vecino is None:  # No se encontró mejor vecino
            break

        solucion_actual = mejor_vecino
        puntaje_actual = mejor_puntaje

    return solucion_actual

def evaluar(solucion):
    # Ejemplo: la suma de los valores nutricionales de los ingredientes con penalización por repetición
    valores_nutricionales = {
        'lechuga': 5,
        'tomate': 10,
        'zanahoria': 8,
        'pepino': 7,
        'aguacate': 15
    }
    puntaje = sum(valores_nutricionales[ingrediente] for ingrediente in solucion)
    penalizacion = (len(solucion) - len(set(solucion))) * 10  # Penalización fuerte por ingredientes repetidos
    return puntaje - penalizacion

def generar_vecinos(solucion):
    ingredientes = ['lechuga', 'tomate', 'zanahoria', 'pepino', 'aguacate']
    vecinos = []
    for i in range(len(solucion)):
        for ingrediente in ingredientes:
            if ingrediente != solucion[i] and ingrediente not in solucion:
                vecino = solucion[:]
                vecino[i] = ingrediente
                vecinos.append(vecino)
    return vecinos

# Ejemplo de uso
solucion_inicial = ['lechuga', 'tomate', 'zanahoria', 'pepino']
mejor_solucion = escalada_colina(solucion_inicial, evaluar, generar_vecinos)
print(f'Mejor solución encontrada: {mejor_solucion}, con puntaje: {evaluar(mejor_solucion)}')