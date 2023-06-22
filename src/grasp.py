from src.tsp import greedy


def grasp(g, inicio, margen, mejora_limite):
    camino_inicial, costo = camino_minimo(g, inicio, margen)

    mejor = camino_inicial
    barato = costo_incial
    mejoras = 0
    vecinos = vecinos_de(mejor)

    for vecino in vecinos:
        peso = peso(vecino, grafo)
        if peso < barato:
            mejor = vecino
            barato = peso
        else:
            mejoras += 1

        if mejoras == mejora_limite:
            return mejor, barato

    return mejor, barato


# O(n^2+2n) = O(n^2)
# Genera la lista de soluciones donde solo cambia un paso
def vecinos_de(res):
    solucion_inicial = res.copy()  # O(n)
    pos_final = len(res) - 1
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

