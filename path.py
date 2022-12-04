import node
import segment
import graph
import math
import matplotlib.pyplot as pyplot

'''
    Path()
    =======
    Defines an empty path
    path_nodes: List of nodes contained in that path
    cost: list of the distances from the origin to each of the nodes in the path
    total_cost: total distance of the path

'''
class Path:
    def __init__(self):
        self.path_nodes = []
        self.cost = []
        self.total_cost = 0.0

'''
    getNodeByName(P: Path(), namenode: str)
    =======================================
    function that recives a path and the name of a node and returns the entire node
    P: path in wich we are searching the node
    nameNode: name of the node we are looking for

'''
def getNodeByName(P, nameNode):
    for i in P.path_nodes:
        if i.name == nameNode:
            return i
    return None

'''
    addNode(G: Graph(), P: Path(), name: str)
    ==========================================
    Function that adds a node to a path by giving the path and node's name
    G: graph that contains the node and the path
    P: path in wich we are going to add the node
    name: name of the node that will be added to the path

'''
def addNode(G, P, name):
    for i in G.Nodes:
        if i.name == name:
            n = i
    if not(n in G.Nodes):
            return False
    if len(P.path_nodes) > 0:
        if not(n in P.path_nodes[-1].neighbours):
            return False
    if n in P.path_nodes:
        print("Error: Node already exists in the Path")
        return False
    else:
        P.path_nodes.append(n)
        if len(P.path_nodes) == 1:
            P.cost.append(P.total_cost + node.distance(P.path_nodes[-1], n))
        else:
            P.cost.append(P.total_cost + node.distance(P.path_nodes[-2], n))
        P.total_cost = P.cost[-1]
        return True

'''
    containsNode(P: Path(), name: str)
    ===================================
    Given a path and the name of a node, 
    returns true if the node belongs to the path, 
    and false otherwise
    P: path in wich we are searching the node
    name: name of the node we are looking for

'''
def containsNode(P, name):
    n = getNodeByName(P, name)
    if n == None:
        return False
    return True
    
'''
    getCostToNode(P: Path(), name: str)
    ====================================
    Given a path and the name of a node, returns the distance (float),
    from the origin of the path to that node.
    P: path in wich we are going to mesure the distance
    node: node to wich we are going to mesure the distance
'''
def getCostToNode(P, name):
    for i in P.path_nodes:
        if i.name == name:
            n = i
    if n in P.path_nodes:
        index = P.path_nodes.index(n)
    cost = P.cost[index]
    return cost

'''
    getApproxToDest(G: Graph(), P: Path(), name: str)
    =================================================
    Given a graph, a path and the name of a node, calculates the aproximation of the distance between
    the last node in the graph and the parameter node (Euclidean distance)
    G: graph that contains the path and all the nodes
    P: path to wich node belongs
    name: name of the destination node

'''
def getApproxToDest(G, P, name):
    for i in G.Nodes:
        if i.name == name:
            n = i
    
    d = math.sqrt((n.x-P.path_nodes[-1].x)**2 + (n.y-P.path_nodes[-1].y)**2)
    return d

'''
    getEstimatedCost(G: Graph(), P: Path(), nameActual: str, nameDest: str)
    ========================================================================
    given the name of the actual node, the destination node, a graph and a path, calculates the total cost from origin
    to the actual node plus the aproximate distance to the destination node
    G: given graph
    P: path that contains the actual node
    nameActual: name of the actual node
    nameDest: name of the destination node
'''
def getEstimatedCost(G, P, nameActual, nameDest):
    d = getCostToNode(P, nameActual) + getApproxToDest(G, P, nameDest)
    return d

'''
    plotPath(G: Graph(), P: Path())
    ===============================
    Given a graph and a path, plots that path in the graph
    G: graph that contains all the nodes of the path
    P: path that belongs to the graph
    return: nothing
'''
def plotPath(G, P):
    for i in P.path_nodes:
        pyplot.scatter(i.x, i.y,s=2**2, color = "black", zorder = 3)
        pyplot.text(i.x, i.y, i.name,  color = "black", size = 5)

    for i in G.Nodes:
        if not(i in P.path_nodes):
            pyplot.scatter(i.x, i.y,s=2**2, color = "grey", zorder = 3)
            pyplot.text(i.x, i.y, i.name,  color = "grey", size = 5)

    for i in range(1, len(P.path_nodes)):
        pyplot.arrow(P.path_nodes[i-1].x, P.path_nodes[i-1].y, P.path_nodes[i].x - P.path_nodes[i-1].x, P.path_nodes[i].y - P.path_nodes[i-1].y, color = "#81F7F5", length_includes_head = True, head_width = 0.05, head_length = 0.05)
        pyplot.text((P.path_nodes[i].x + P.path_nodes[i-1].x)/2 , (P.path_nodes[i].y + P.path_nodes[i-1].y)/2, round(node.distance(P.path_nodes[i-1], P.path_nodes[i]),2), size=5)
    pyplot.title("PATH FROM " + P.path_nodes[0].name + " TO " + P.path_nodes[-1].name + " COST = " + str(round(P.total_cost, 3)))
    pyplot.show()

'''
    pathToKML(path: Path(), filename: string)
    =========================================
    Builds a KML file with the given file name adds the points and segments given on the path
    path: path that has to be ploted on google earth
    filename: string, the name of the KML file
    return: nothing
'''
def pathToKML(path, filename):
    with open(filename + ".kml", "w") as f:

        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">")
        f.write("<Document>")
        f.write("<Placemark>")
        f.write("<name>Exported Path</name>")
        f.write("<LineString>")
        f.write("<coordinates>")

        i = 0
        while i < len(path.path_nodes):
            text = str(path.path_nodes[i].x) + "," + str(path.path_nodes[i].y) + ",0"
            if i < len(path.path_nodes) - 1:
                text += ","
            f.write(text)
            i += 1

        f.write("</coordinates>")
        f.write("</LineString>")
        f.write("</Placemark>")
        f.write("</Document>")
        f.write("</kml>")