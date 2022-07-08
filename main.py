from networkx import from_numpy_matrix
from src.importer import get_graph
from src.grasp import grasp

if __name__ == '__main__':
    #nombre_test = 'brg180.xml'
    print('ingrese nombre del archivo:')
    nombre_test=input()
    G = get_graph(nombre_test+'.xml')
    graph = from_numpy_matrix(G)
    camino, valor = grasp(graph, 0, 3, 3)
    with open('resultado.txt', 'w') as file:
        file.write("Problema: " + nombre_test + '\n')
        file.write("Camino hamiltoniano: " + str(camino) + '\n')
        file.write("Valor: " + str(valor))
        file.close()
    print('resultado generado')
