# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.grasp import startGrasp
from src.importer import start_graph

GRAPH_LABEL = 'graph'
VERTEX_LABEL = 'vertex'
EDGES_LABEL = 'edge'
COST_LABEL = 'cost'
root=""




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #startGrasp("asd")
    source='sample/' #input()

    start_graph(source)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
