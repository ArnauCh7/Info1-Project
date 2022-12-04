import node

"""
    Segment(org: Node, dest: Node)
    ==============================
    class for a segment that have a distance in it and two nodes, the origin and destination
    org: origin node
    dest: destination node
    cost: distance between those two nodes

"""
class Segment:
    def __init__(self, org, dest):
        self.org = org
        self.dest = dest
        self.cost = node.distance(org, dest)