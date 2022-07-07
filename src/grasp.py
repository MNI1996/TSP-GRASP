from src.importer import create_graph
from src.tsp import tsp,TPS_Vecinos

def startGrasp(data,origen,margen):
    #armo mi grafo con el importer
    grafo=create_graph(data)
    #armo mi solucion inicial con tsp
    best=tsp(grafo,origen,margen)
    n=0
    res=None
    flag=True
    #while algo:
    while flag:
        if n%5 !=0 :
            # armo mi busqueda local en base a mi solucion tsp y la comparo con mi busqueda inicial
            nbest = TPS_Vecinos(grafo,best,margen)
        else :
            if best[0]< nbest:
                res = nbest
            else:
                flag=False
    return res
