import node
import segment
import path
import math
import matplotlib.pyplot as pyplot

"""
    Graph()
    =======
    empty graph
    Nodes: list of nodes that are going to be on the graph
    Segments: list of segments that are going to relate those nodes

"""
class Graph:
    def __init__(self):
        self.Nodes = []
        self.Segments = []

"""
    addNode(G: Graph, N: Node)
    ==========================
    function that adds a node(N) to the list of nodes in the graph(G)
    G: graph created earlier
    N: node tha's going to be added to the graph

"""
def addNode(G, N):
    for i in G.Nodes:
        if N.name == i.name:
            return False
    G.Nodes.append(N)
    return True

'''
    getNodeByName(G: Graph(), nameNode: str)
    ========================================
    given a graph and the name of a node, searches the node on the graph and returns the entire node
    G: given graph
    nameNode: the name of the node we are looking for
'''
def getNodeByName(G, nameNode):
    for i in G.Nodes:
        if i.name == nameNode:
            return i
    return None

"""
    addSegments(G: Graph, nameOrg: str, nameDst: str)
    =================================================
    function that adds segments to the segment list of the grap(G) 
    by giving the names of the nodes that make the segment
    G: graph created earlier
    nameOrg: name of the origin node
    nameDst: name of the destiny node

"""
def addSegment(G, nameOrg, nameDst):
    org = getNodeByName(G, nameOrg)
    dest =getNodeByName(G, nameDst)
    if org == None or dest == None:
        return False
    if not(node.addNeighbour(org,dest)):
        return False
    seg = segment.Segment(org, dest)
    for i in G.Segments:
        if seg.org.name == i.org.name and seg.dest.name == i.dest.name:
            return False
    G.Segments.append(seg)
    return True

"""
    plot(G: Graph)
    ==============
    plots the graph wich we added all the nodes and segments
    G: graph with all the segments and nodes added

"""
def plot(G):
    for i in G.Segments:
        pyplot.arrow(i.org.x, i.org.y, i.dest.x - i.org.x, i.dest.y - i.org.y,  color = "#81F7F5", length_includes_head = True, head_width = 0.05, head_length = 0.05)
        pyplot.text((i.org.x + i.dest.x)/2 , (i.org.y + i.dest.y)/2, round(i.cost, 2), size=5)
        
    for i in G.Nodes:
        pyplot.scatter(i.x, i.y, color = "black", s = 2**2, zorder = 3)
        pyplot.text(i.x, i.y, i.name, size=5)
    pyplot.title("AIRSPACE GRAPHIC")
    pyplot.grid(b=None, which='major', axis='both', color = "red", linewidth=0.5, linestyle=':')
    pyplot.show()

"""
    plotNode(G: Graph , name: str)
    =================
    plots all the nodes of the graph resalting the node we selected (name) and it's neighbours
    and plots only the segments of this node to the neighbours
    G: given graph
    name: name of the node we selected
"""
def plotNode(G,name):
    n = getNodeByName(G, name)
    if n == None:
        return

    for i in n.neighbours:
        s = segment.Segment(n,i)
        pyplot.arrow(n.x, n.y, i.x - n.x, i.y - n.y,  color = "#81F7F5", length_includes_head = True, head_width = 0.05, head_length = 0.05)
        pyplot.text((n.x + i.x)/2 , (n.y + i.y)/2, round(s.cost, 2), size = 5)

    for i in G.Nodes:
        if i.name == name:
            pyplot.scatter(i.x, i.y, s=2**2, color = "red", zorder = 3)
            pyplot.text(i.x, i.y, i.name, color ="red", size = 5)
        else:
            pyplot.scatter(i.x, i.y, s = 2**2 ,color = "grey", zorder = 3)
            pyplot.text(i.x, i.y, i.name, color = "grey", size = 5)
    pyplot.title(name + "NEIGHBOURS GRAPHIC")
    pyplot.show()

'''
    findShortestPath(G: Graph(), nameOrg: str, nameDst: str)
    ========================================================
    Given a graph, the name of the origin node and the name of the destination node 
    returns the shortest path from the origin node to the destination node.
    G: graph where we are going to plot the path
    nameOrg: name of the origin node of the path
    nameDst: name of the destination node of the path

'''
def findShortestPath(G, nameOrg, nameDst):
    nodeOrg = getNodeByName(G, nameOrg)
    nodeDst = getNodeByName(G, nameDst)

    if not nodeOrg or not nodeDst:
        print("One or both of the given nodes do not exists in the specified graph")
        return None

    paths = []
    ended = False

    savedPath = path.Path()
    path.addNode(G, savedPath, nodeOrg.name)

    paths.append(savedPath)
    while len(paths) > 0 and not ended:
        i = 0
        bestIndex = 0
        while i < len(paths):
            lastNode = paths[i].path_nodes[-1]
            lastBestNode = paths[bestIndex].path_nodes[-1]
            if path.getEstimatedCost(G, paths[i], lastNode.name, nameDst) < path.getEstimatedCost(G, paths[bestIndex], lastBestNode.name, nameDst):
                bestIndex = i
            i += 1

        savedPath = paths[bestIndex]
        paths.remove(savedPath)
        i = 0
        while i < len(savedPath.path_nodes[-1].neighbours):
            neigh = savedPath.path_nodes[-1].neighbours[i]
            if neigh.name == nameDst:
                path.addNode(G, savedPath, neigh.name)
                ended = True
                break
            else:
                if not path.containsNode(savedPath, neigh.name): # do nothing
                    temp = path.Path()

                    k = 0
                    while k < len(savedPath.path_nodes):
                        temp.path_nodes.append(savedPath.path_nodes[k])
                        k += 1

                    k = 0
                    while k < len(savedPath.cost):
                        temp.cost.append(savedPath.cost[k])
                        k += 1

                    temp.total_cost = savedPath.total_cost

                    path.addNode(G, temp, neigh.name)

                    better = True
                    for onePath in paths:
                        if not path.containsNode(onePath, neigh.name):
                            continue

                        if path.getCostToNode(onePath, neigh.name) < path.getCostToNode(temp, neigh.name):
                            better = False
                            break
                        else:
                            paths.remove(onePath)

                    if better:
                        paths.append(temp)

            i += 1
    return savedPath
