import airSpace
import graph
import path
""" ===========================================================================================
 Program to test the airspace classes
"""
A = airSpace.buildAirSpace("Spain")
G = airSpace.buildAirGraph(A)
print("Testing...")
graph.plot(G)
graph.plotNode(G,"GODOX")
c = graph.findShortestPath(G,"LEBL","LEZG")
path.plotPath(G,c)
print("OK")
