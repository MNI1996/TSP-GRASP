import pathlib

from src.graph import generateMatrix,printGraph
from xml.etree import ElementTree as ET
import sys


GRAPH_LABEL = 'graph'
VERTEX_LABEL = 'vertex'
EDGES_LABEL = 'edge'
COST_LABEL = 'cost'
#DATASET = 'gr24.xml'
#FILE_PATH="D:\Facultad\Algoritmos\TSP-GRASP\sample\ "
#FULL_FILE_PATH= FILE_PATH+DATASET
#tree = ET.parse(FULL_FILE_PATH)
#root = tree.getroot()

def filter_xmlelements(elem, tag):
  print(elem)
  return list(filter(lambda x: x.tag == tag, elem.getchildren()))

def get_cost_from_xmledge(xmledge):
  cost = xmledge.get(COST_LABEL)
  return float(cost)

def get_edges_from_xmlvertex(xmlvertex):
  xmledges = xmlvertex.getchildren()
  return list(map(get_cost_from_xmledge, xmledges))

def get_graph_from_xmlgraph(xmlgraph):
  xmlvertexes = filter_xmlelements(xmlgraph, VERTEX_LABEL)
  total_vertexes = len(xmlvertexes)
  graph = generateMatrix(total_vertexes, total_vertexes)

  for vertex_index, xmlvertex in enumerate(xmlvertexes):
    graph[vertex_index] = get_edges_from_xmlvertex(xmlvertex)
  return graph


def start_graph(source):
  DATASET = 'gr24.xml'
  FILE_PATH = source
  FULL_FILE_PATH =FILE_PATH+DATASET
  tree = ET.parse(FULL_FILE_PATH)
  root = tree.getroot()
  xmlgraph = filter_xmlelements(root, GRAPH_LABEL)[0]
  graph = get_graph_from_xmlgraph(xmlgraph)
  printGraph(graph)