from src.tsp import greedy


def grasp(grafo, inicio, margen, limite_sin_mejorar):
    camino_inicial, costo_incial = greedy(grafo, inicio, margen)

    mejor_camino = camino_inicial
    mejor_costo = costo_incial
    veces_sin_mejorar = 0
    vecinos = vecinos_de(mejor_camino)

    for vecino in vecinos:
        peso = peso_de(vecino, grafo)
        if peso < mejor_costo:
            mejor_costo = peso
            mejor_camino = vecino
        else:
            veces_sin_mejorar += 1

        if veces_sin_mejorar == limite_sin_mejorar:
            return mejor_camino, mejor_costo

    return mejor_camino, mejor_costo


# O(n^2+2n) = O(n^2)
# Genera la lista de soluciones donde solo cambia un paso
def vecinos_de(solucion):
    solucion_inicial = solucion.copy()  # O(n)
    pos_final = len(solucion) - 1
    elemento_inicial_final = solucion[0]
    # Saco el primer y el ultimo elemento,ya que es donde inicio el recorrido
    solucion_inicial.pop(0)
    solucion_inicial.pop(pos_final - 1)
    soluciones = []

    # O(n*n)
    for i in range(len(solucion_inicial) - 1):  # O(n):
        sol_parcial = solucion_inicial.copy()  # O(n)
        sol_parcial[i] = solucion_inicial[i+1]
        sol_parcial[i+1] = solucion_inicial[i]
        # Agrego el primer elemento al principio y al final, ya que es donde el recorrido debe empezar y terminar
        soluciones.append([elemento_inicial_final] + sol_parcial + [elemento_inicial_final])

    sol_parcial = solucion_inicial.copy()  # O(n)
    sol_parcial[0] = solucion_inicial[pos_final - 2]
    sol_parcial[pos_final - 2] = solucion_inicial[0]
    soluciones.append([elemento_inicial_final] + sol_parcial + [elemento_inicial_final])

    return soluciones


# O(n)
def peso_de(camino, grafo):
    peso_total = 0

    # O(n): recorre una solucion que contiene n-1 vertices
    for i in range(len(camino) - 1):
        actual = grafo[camino[i]]
        siguiente = camino[i+1]
        peso_total += actual[siguiente]['weight']

    return peso_total

