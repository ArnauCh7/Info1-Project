import node

N1 = node.Node("A", 3, 5)
N2 = node.Node("B", 5, 7)
N3 =node.Node("B", 4, 5)
print(node.addNeighbour(N1, N2))
print(node.addNeighbour(N1, N3))

