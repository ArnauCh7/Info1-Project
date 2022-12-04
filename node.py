import math

"""
    Node (name: str, x:float, y:float)
    ==================================
    Defines a class Node wich is a position in 2D
    name: string, name of the node
    x: float, x cordinate of the point position
    y: float, y cordinate of the point position
    neighbours: list of the neighbour nodes

"""
class Node:
    def __init__(self, name, x, y):
        self.name = str(name)
        self.x = float(x)
        self.y = float(y)
        self.neighbours = []

"""
    addNeighbour(n: Node, nd: Node)
    ===============================
    Defines a function that adds a node to the neighbour list of another node
    n: node wich we are going to add a neighbour to
    nd: the neighbour node we are going to add

"""

def addNeighbour(n, nd):
    if n.name == nd.name:
        return False
    for i in n.neighbours:
        if i.name == nd.name:
            return False
    n.neighbours.append(nd)
    return True

"""
    distance(n1: Node, n2: Node)
    ============================
    function wich calculates the distance between node 1 and node 2
    n1: starting node
    n2: final node

"""
def distance (n1, n2):
    try:   
        lat1 = n1.y
        lon1 = n1.x
        lat2 = n2.y
        lon2 = n2.x
        lat1 = lat1*math.pi/180.0
        lon1 = lon1*math.pi/180.0
        lat2 = lat2*math.pi/180.0
        lon2 = lon2*math.pi/180.0
        dLon = lon1-lon2
        return math.acos (math.sin(lat1) * math.sin(lat2) + math.cos(lat1)* math.cos(lat2) * math.cos(dLon) ) * 6378.137
    except:
        return -1
