import graph
import node
import path
import airSpace

'''
    Graph that's loaded 
'''

loadedGraph = False

'''
    Airspace that's loaded
'''

loadedAirspace = False

''' createSimpleGraph ():
 =========================
 Creates a simple graph with nodes and segments
 return: Graph, the graph created
'''

def createSimpleGraph():
 G = graph.Graph()
 graph.addNode(G, node.Node("A",1,20))
 graph.addNode(G, node.Node("B",8,17))
 graph.addNode(G, node.Node("C",15,20))
 graph.addNode(G, node.Node("D",18,15))
 graph.addNode(G, node.Node("E",2,4))
 graph.addNode(G, node.Node("F",6,5))
 graph.addNode(G, node.Node("G",12,12))
 graph.addNode(G, node.Node("H",10,3))
 graph.addNode(G, node.Node("I",19,1))
 graph.addNode(G, node.Node("J",13,5))
 graph.addNode(G, node.Node("K",3,15))
 graph.addNode(G, node.Node("L",4,10))
 graph.addSegment(G, "A","B")
 graph.addSegment(G, "A","E")
 graph.addSegment(G, "A","K")
 graph.addSegment(G, "B","A")
 graph.addSegment(G, "B","C")
 graph.addSegment(G, "B","F")
 graph.addSegment(G, "B","K")
 graph.addSegment(G, "B","G")
 graph.addSegment(G, "C","D")
 graph.addSegment(G, "C","G")
 graph.addSegment(G, "D","G")
 graph.addSegment(G, "D","H")
 graph.addSegment(G, "D","I")
 graph.addSegment(G, "E","F")
 graph.addSegment(G, "F","L")
 graph.addSegment(G, "G","B")
 graph.addSegment(G, "G","F")
 graph.addSegment(G, "G","H")
 graph.addSegment(G, "I","D")
 graph.addSegment(G, "I","J")
 graph.addSegment(G, "J","I")
 graph.addSegment(G, "K","A")
 graph.addSegment(G, "K","L")
 graph.addSegment(G, "L","K")
 graph.addSegment(G, "L","F")

 return G

''' printInstructions ():
 =========================
 Prints the menu on the terminal
 Doesn't return anything
'''
def printInstructions():
    print("Main menu")
    print("======================================================================")
    print("a - Load simple graph (i.e. the first week graph)")
    print("b - Plot graph")
    print("c - Plot node (ask node name)")
    print("d - Plot path (ask list of nodes to form the path)")
    print("e - Plot min path (ask origin node and destination node)")
    print("---------------------")
    print("f - Load airspace (ask airspace name)")
    print("g - List airports")
    print("h - Create airports.kml (ask name of the output file)")
    print("i - Create route.kml (ask name of the output file)")
    print("---------------------")
    print("z - Exit")

''' printGraphNodes (G: Graph):
    =========================
    Prints nodes of the given graph
    G: Graph, the graph which nodes are meant to be printed
    Doesn't return anything
'''
def printGraphNodes(G):
    i = 0
    while i < len(G.Nodes):
        print("Node #" + str(i + 1) + ": " + G.Nodes[i].name)
        i += 1

''' executeOption (option: string):
    =========================
    Executes the given option and returns the result
    option: string, the option to be executed, i.e. f
    returns a boolean, the result of the process, True if everything is fine and we can display again the menu instructions,
            False if we cannot display the menu instructions because of an error or other reasons
'''
def executeOption(option):
    global loadedGraph
    global loadedAirspace

    if option == 'a':
        loadedGraph = createSimpleGraph()
        return True
    elif option == 'b':
        if not loadedGraph:
            print("There's no loaded graph yet! (i.e. Use option a)")
            return False
        else:
            graph.plot(loadedGraph)
            return True
    elif option == 'c':
        if not loadedGraph:
            print("There's no loaded graph yet! (i.e. Use option a)")
            return False
        else:
            printGraphNodes(loadedGraph)
            nodeName = input("Enter the node name to plot from the previous options:   ")
            exitLoop = False
            while not graph.getNodeByName(loadedGraph, nodeName) and not exitLoop:
                print("Could not find any node with that name!")
                nodeName = input("Enter the node name to plot from the previous options (quit to exit):   ")
                if nodeName == 'quit':
                    exitLoop = True

            if exitLoop:
                return True

            graph.plotNode(loadedGraph, nodeName)
            return True
        return True
    elif option == 'd':
        if not loadedGraph:
            print("There's no loaded graph yet! (i.e. Use option a)")
            return False
        else:
            printGraphNodes(loadedGraph)
            P = path.Path()
            exitLoop = False
            while not exitLoop:
                nodeName = input("Enter the next path node from the previous node options (empty to quit):   ")
                if len(nodeName) <= 0:
                    exitLoop = True
                else:
                    if not graph.getNodeByName(loadedGraph, nodeName):
                        print("Could not find any node with that name!")
                    else:
                        res = path.addNode(loadedGraph, P, nodeName)
                        if not res:
                            print("Could not add to the path that node! It may be already in the path or not be a"
                                  "neighbour of the last node.")

            if len(P.path_nodes) <= 0:
                print("Cannot plot an empty path!")
                return True
            else:
                path.plotPath(loadedGraph, P)
        return True
    elif option == 'e':
        if not loadedGraph:
            print("There's no loaded graph yet! (i.e. Use option a)")
            return False
        else:
            printGraphNodes(loadedGraph)

            origin = input("Enter the origin node from the previous options:   ")
            exitLoop = False
            while not graph.getNodeByName(loadedGraph, origin) and not exitLoop:
                print("Could not find any node with that name!")
                origin = input("Enter the origin node from the previous options (quit to exit):   ")
                if origin == 'quit':
                    exitLoop = True

            if exitLoop:
                return True

            destination = input("Enter the destination node from the previous options:   ")
            exitLoop = False
            while not graph.getNodeByName(loadedGraph, destination) and not exitLoop:
                print("Could not find any node with that name!")
                origin = input("Enter the destination node from the previous options (quit to exit):   ")
                if origin == 'quit':
                    exitLoop = True

            if exitLoop:
                return True

            P = graph.findShortestPath(loadedGraph, origin, destination)
            if P is None:
                print("Could not find any path between those nodes!")
            else:
                path.plotPath(loadedGraph, P)

        return True
    elif option == 'f':
        name = input("Enter the airspace name to load:   ")
        loadedAirspace = airSpace.buildAirSpace(name)
        return True
    elif option == 'g':
        if not loadedAirspace:
            print("There's no loaded airspace yet! (i.e. use option f)")
            return False
        else:
            i = 0
            while i < len(loadedAirspace.navAirports):
                print("Airport #" + str(i + 1) + ": " + loadedAirspace.navAirports[i].name)
                i += 1
        return False 

    elif option == 'h':
        if not loadedAirspace:
            print("There's no loaded airspace yet! (i.e. use option f)")
            return False
        else:
            name = input("Enter name of the file to store the airports in KML:   ")
            airSpace.airportsToKML(loadedAirspace, name)
        return True
    elif option == 'i':
        if not loadedAirspace:
            print("There's no loaded airspace yet! (i.e. use option f)")
            return False
        else:
            name = input("Enter name of the file to store the path in KML:   ")

            origin = input("Enter the origin navigation point or airport for the route:   ")
            exitLoop = False
            while not airSpace.getPointByName(loadedAirspace, origin) and not exitLoop:
                print("Could not find any point with that name!")
                origin = input("Enter the origin navigation point or airport for the route: (quit to exit):   ")
                if origin == 'quit':
                    exitLoop = True

            if exitLoop:
                return True

            destination = input("Enter the destination navigation point or airport for the route:   ")
            exitLoop = False
            while not airSpace.getPointByName(loadedAirspace, destination) and not exitLoop:
                print("Could not find any point with that name!")
                origin = input("Enter the destination navigation point or airport for the route: (quit to exit):   ")
                if origin == 'quit':
                    exitLoop = True

            if exitLoop:
                return True

            G = airSpace.buildAirGraph(loadedAirspace)
            P = graph.findShortestPath(G, origin, destination)

            if P is None:
                print("Could not find any path between those nodes!")
            else:
                path.pathToKML(P, name)
        return True
    return False

''' startMenu ():
 =========================
 Starts the execution of the user menu
 Doesn't return anything
'''
def startMenu():
    printInstructions()
    exitMenu = False
    while not exitMenu:
        choice = input("Select an option:   ")
        if choice == 'z':
            exitMenu = True
        elif executeOption(choice):
            printInstructions()
startMenu()