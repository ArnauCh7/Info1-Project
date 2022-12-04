import navSegment
import navPoint
import navAirport
import graph
import node

""" Airspace ()
 ===========================
 Defines class Airspace defined by an array of NavPoints, an array of NavSegments between the NavPoints and
    the NavAirports
 navPoints: NavPoint[], array of NavPoint
 navSegments: NavSegment[], array of NavPSegment
 navAirports: NavAirport[], array of NavAirport
"""
class Airspace:
    def __init__(self):
        self.navPoints = []
        self.navSegments = []
        self.navAirports = []

""" getPointByName (air: Airspace, name: string): NavPoint
 =========================
 Returns the NavPoint with the specified name, False if not found
 air: Airspace, airspace the NavPoint belongs to.
 name: string, name of the NavPoint.
 return: NavPoint, the point with the specified name
"""
def getPointByName(air, name):
    i = 0
    while i < len(air.navPoints):
        if air.navPoints[i].name == name:
            return air.navPoints[i]
        i += 1
    return False

""" getPointByNum (air: Airspace, num: number): NavPoint
 =========================
 Returns the NavPoint with the specified number, False if not found
 air: Airspace, airspace the NavPoint belongs to.
 num: number, number of the NavPoint.
 return: NavPoint, the point with the specified number
"""
def getPointByNum(air, num):
    i = 0
    while i < len(air.navPoints):
        if air.navPoints[i].num == num:
            return air.navPoints[i]
        i += 1
    return False

""" getAirportByName (air: Airspace, name: string): NavAirport
 =========================
 Returns the NavPoint with the specified number, False if not found
 air: Airspace, airspace the Airport belongs to.
 name: string, name of the NavAirport.
 return: NavAirport, the NavAirport with the specified number
"""
def getAirportByName(air, name):
    i = 0
    while i < len(air.navPoints):
        if air.navAirports[i].name == name:
            return air.navAirports[i]
        i += 1
    return False

""" addPoint (air: Airspace, point: NavPoint): void
 =========================
 Adds the specified NavPoint to the specified airspace
 air: Airspace, airspace the Airport belongs to.
 point: NavPoint, the NavPoint to be added
 return: nothing.
"""
def addPoint(air, point):
    air.navPoints.append(point)

""" addSegment (air: Airspace, numOrig: number, numDst: number, distance: float): void
 =========================
 Adds the specified NavPoint to the specified airspace
 air: Airspace, airspace the Segment belongs to.
 numOrig: number, the number of the origin NavPoint
 numDst: number, the number of the destination NavPoint
 distance: float, distance between origin and destination NavPoints
 return: nothing.
"""
def addSegment(air, numOrig, numDst, distance):
    S = navSegment.NavSegment(numOrig, numDst, distance)
    air.navSegments.append(S)

""" addAirport (air: Airspace, name: string): void
 =========================
 Adds the specified NavAirport to the specified airspace
 air: Airspace, airspace the NavAirport belongs to.
 name: string, the name of the airport
 return: nothing.
"""
def addAirport(air, name):
    A = navAirport.NavAirport(name)
    air.navAirports.append(A)

""" addSID (air: Airspace, nameAirport: string, nameSID: string): void
 =========================
 Receives an AirSpace (air) and the name (name) of an airport and the name of a
    navigation point (nameSID). Adds the point as a SID of the airport.
 air: Airspace, airspace the SID belongs to
 nameAirport: string, name of the airport to add the SID
 nameSID: string, name of the SID to be added
 return: nothing.
"""
def addSID(air, nameAirport, nameSID):
    airport = getAirportByName(air, nameAirport)
    pointSID = getPointByName(air, nameSID)
    if not airport or not pointSID:
        return
    else:
        if len(airport.SIDs) <= 0: 
            airportLat = pointSID.lat
            airportLon = pointSID.lon

            airportPoint = navPoint.NavPoint(-1, nameAirport, airportLat, airportLon)
            addPoint(air, airportPoint) 

        airport.SIDs.append(pointSID)

""" addSTAR (air: Airspace, nameAirport: string, nameSTAR: string): void
 =========================
 Receives an AirSpace (air) and the name (name) of an airport and the name of a
    navigation point (nameSTAR). Adds the point as a STAR of the airport.
 air: Airspace, airspace the STAR belongs to
 nameAirport: string, name of the airport to add the STAR
 nameSTAR: string, name of the STAR to be added
 return: nothing.
"""
def addSTAR(air, nameAirport, nameSTAR):
    airport = getAirportByName(air, nameAirport)
    pointSTAR = getPointByName(air, nameSTAR)
    if not airport or not pointSTAR:
        return
    else:
        airport.STARs.append(pointSTAR)

""" loadNavPoints (air: Airspace, filename: string): void
 =========================
 Loads the NavPoints from the specified file to the specified Airspace.
 air: Airspace, airspace to add the NavPoints
 filename: string, name of the file that stores the NavPoints
 return: nothing.
"""
def loadNavPoints(air, filename):
    with open(filename) as f:
        for line in f:
            items = line.strip().split(" ")

            num = items[0]
            name = items[1]
            lat = items[2]
            lon = items[3]

            P = navPoint.NavPoint(int(num), name, float(lat), float(lon))
            addPoint(air, P)

""" loadSegments (air: Airspace, filename: string): void
 =========================
 Loads the NavSegments from the specified file to the specified Airspace.
 air: Airspace, airspace to add the NavSegment
 filename: string, name of the file that stores the NavSegments
 return: nothing.
"""
def loadSegments(air, filename):
    with open(filename) as f:
        for line in f:
            items = line.strip().split(" ")

            origNum = items[0]
            dstNum = items[1]
            distance = items[2]

            addSegment(air, int(origNum), int(dstNum), float(distance))

""" loadAirports (air: Airspace, filename: string): void
 =========================
 Loads the NavAirports from the specified file to the specified Airspace.
 air: Airspace, airspace to add the NavAirports
 filename: string, name of the file that stores the NavAirports
 return: nothing.
"""
def loadAirports(air, filename):
    with open(filename) as f:
        i = 0
        airport = "" 
        for line in f:
            if i == 0:
                airport = line.strip()
                addAirport(air, airport)
            elif i == 1:
                departure = line.strip().split(" ")
                j = 0
                while j < len(departure):
                    point = getPointByName(air, departure[j])
                    if not point:
                        j += 1
                        continue
                    else:
                        addSID(air, airport, departure[j])
                    j += 1
            elif i == 2:
                arrival = line.strip().split(" ")
                j = 0
                while j < len(arrival):
                    point = getPointByName(air, arrival[j])
                    if not point:
                        j += 1
                        continue
                    else:
                        addSTAR(air, airport, arrival[j])
                    j += 1
            i += 1
            if i == 3:
                currentAirport = getAirportByName(air, airport)
                if currentAirport != False:
                    if len(currentAirport.SIDs) <= 0 or len(currentAirport.STARs) <= 0:
                        air.navAirports.remove(currentAirport)
                airport = ""
                i = 0

""" buildAirSpace (filename: string): Airspace
 =========================
 Builds an Airspace from the specified files and returns it.
 filename: name, the partial name of the desired files to load. Preffix of the location, i.e. Cat, Spain...
 return: Airspace, the built Airspace
"""
def buildAirSpace(filename):
    A = Airspace()

    try:
        loadNavPoints(A, filename + "_nav.txt")
    except Exception as e:
        print("ERROR! Could not load NavPoints: ", e)
    
    try:
        loadSegments(A, filename + "_seg.txt")
    except Exception as e:
        print("ERROR! Could not load NavPoints: ", e)
    
    try:
        loadAirports(A, filename + "_aer.txt")
    except Exception as e:
        print("ERROR! Could not load NavPoints: ", e)

    return A

""" buildAirGraph (air: Airspace): Graph
 =========================
 Builds a Graph with the given airspace, adding the nodes and segments.
 air: Airspace, the airspace to get the Graph from
 return: Graph, the graph built from the Airspace
"""
def buildAirGraph(air):
    G = graph.Graph()

    i = 0
    while i < len(air.navPoints):
        graph.addNode(G, node.Node(air.navPoints[i].name, air.navPoints[i].lon, air.navPoints[i].lat))
        i += 1

    i = 0
    while i < len(air.navAirports):
        nodeAirport = node.Node(air.navAirports[i].name, air.navAirports[i].SIDs[0].lon, air.navAirports[i].SIDs[0].lat)
        graph.addNode(G, nodeAirport)

        j = 0
        while j < len(air.navAirports[i].SIDs):
            graph.addSegment(G, nodeAirport.name, air.navAirports[i].SIDs[j].name)
            if G.Segments[-1].cost == -1:
                G.Segments.remove(G.Segments[-1])
            j += 1

        j = 0
        while j < len(air.navAirports[i].STARs):
            graph.addSegment(G, air.navAirports[i].STARs[j].name, nodeAirport.name)
            if G.Segments[-1].cost == -1:
                G.Segments.remove(G.Segments[-1])
            j += 1

        i += 1

    i = 0
    while i < len(air.navSegments):
        origin = getPointByNum(air, air.navSegments[i].orig)
        destination = getPointByNum(air, air.navSegments[i].dst)

        if not origin or not destination:
            i += 1
            continue

        graph.addSegment(G, origin.name, destination.name)
        i += 1
    return G

""" airportsToKML (air: Airspace, filename: string):
 =========================
 Builds a KML file with the given file name with the position of all the airports of the given Airspace
 air: Airspace, the airspace to get the airports
 filename: string, the name of the KML file
 return: nothing
"""
def airportsToKML(air, filename):
    with open(filename + ".kml", "w") as f:
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">")
        f.write("<Document>")

        i = 0
        while i < len(air.navAirports):
            f.write("<Placemark>")
            f.write("<name>" + air.navAirports[i].name + "</name>")
            f.write("<description>" + air.navAirports[i].name + "</description>")
            f.write("<Point>")
            f.write("<coordinates>" + str(air.navAirports[i].SIDs[0].lon) + "," + str(air.navAirports[i].SIDs[0].lat) +
                    ",0</coordinates>")
            f.write("</Point>")
            f.write("</Placemark>")
            i += 1

        f.write("</Document>")
        f.write("</kml>")