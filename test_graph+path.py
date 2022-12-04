import node
import graph
import path
import segment

'''
=====================================================
Programa de pruebas de la fase 2 completa

'''
def creteGraph():
    G = graph.Graph()
    graph.addNode(G, node.Node("A", 1, 20))
    graph.addNode(G, node.Node("B", 8, 17))
    graph.addNode(G, node.Node("C", 15, 20))
    graph.addNode(G, node.Node("D", 18, 15))
    graph.addNode(G, node.Node("E", 2, 4))
    graph.addNode(G, node.Node("F", 6, 5))
    graph.addNode(G, node.Node("G", 12, 12))
    graph.addNode(G, node.Node("H", 10, 3))
    graph.addNode(G, node.Node("I", 19, 1))
    graph.addNode(G, node.Node("J", 13, 5))
    graph.addNode(G, node.Node("K", 3, 15))
    graph.addNode(G, node.Node("L", 4, 10))
    graph.addSegment(G, "A", "B")
    graph.addSegment(G, "A", "E")
    graph.addSegment(G, "A", "K")
    graph.addSegment(G, "B", "A")
    graph.addSegment(G, "B", "C")
    graph.addSegment(G, "B", "F")
    graph.addSegment(G, "B", "K")
    graph.addSegment(G, "B", "G")
    graph.addSegment(G, "C", "D")
    graph.addSegment(G, "C", "G")
    graph.addSegment(G, "D", "G")
    graph.addSegment(G, "D", "H")
    graph.addSegment(G, "D", "I")
    graph.addSegment(G, "E", "F")
    graph.addSegment(G, "F", "L")
    graph.addSegment(G, "G", "B")
    graph.addSegment(G, "G", "F")
    graph.addSegment(G, "G", "H")
    graph.addSegment(G, "I", "D")
    graph.addSegment(G, "I", "J")
    graph.addSegment(G, "J", "I")
    graph.addSegment(G, "K", "A")
    graph.addSegment(G, "K", "L")
    graph.addSegment(G, "L", "K")
    graph.addSegment(G, "L", "F")
    return G

#origen = str(input("Origen: "))
#destino = str(input("Destino: "))
G = creteGraph()
P = graph.findShortestPath(G, "F", "E")
path.plotPath(G, P)
