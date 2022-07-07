import random


def ady(origen,aristas): #O(n)
  return filter((lambda a: a.origen == origen), aristas)


def tsp(grafo, origen, margen):
    res = 0
    adyacentes = ady(origen, grafo.aristas)
    vertices = grafo.vertices
    tour = []
    while len(vertices - origen) > 0: #O(n)
        elem = list(adyacentes).sort(key=(lambda a: a.dist))
        sublist = elem[0:margen]
        choosen = sublist[random.randint(0, margen)]
        res += choosen.dist
        tour.append(choosen.destiny)
        adyacentes = ady(choosen.destiny, grafo.aristas)
        set(vertices)-set(choosen.destiny)
    return res, tour


#vecinos
def search(i,j,aristas):
    res = filter((lambda a: a.origen == i and a.destino == j), aristas)
    return res.peso

def sum_aristas(ls,grafo): #O(n)
    i=0
    j=1
    res=0
    for j in range(len(ls)):
        arista = search(ls[i], ls[j], grafo)
        res += arista
        i += 1
        res += search(ls[0], ls[j], grafo)
    return res


def TPS_Vecinos(grafo, best, limite):#best=(int,[vertices])
    n_best = best
    n=0
    while n > limite or n_best[0] < best[0]: #O(n) donde n es la cantidad de vertices
        shuffle = random.sample(best[1], len(best[1]))
        res_shuffle = sum_aristas(shuffle, grafo)
        if res_shuffle-best[0]>0:
          n_best = (res_shuffle, shuffle)
        n += 1
    return n_best