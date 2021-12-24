# Describes the Königsberg bridges as a graph

# A graph has Vertices and Edges
# every land is a vertex (N, S, E, W) and every bridge is an edge (1,2,3,4,5,6,7)

# To describe a second edge existing between two vertices, we need to add a third vertex
# Nord = 1
# West = 2
# Est = 3
# Sud = 4
# NW = 5 , new vertex between Nord and West
# SW = 6 , new vertex between Sud and West

graph = {
    1: [2,3,5], # vertex conencted to 1
    2: [1,3,4,5,6], # vertex conencted to 2
    3: [1,2,4], # vertex conencted to 3
    4: [2,3,6], # vertex conencted to 4
    5: [1,2], # vertex conencted to 5
    6: [2,4] # vertex conencted to 6
}

def isEulerianPath(graph:list[list[int]]):  
    vertexesWithOddEdges = 0
    for(vertex, edges) in graph.items():
        if len(edges) % 2 == 1:
            vertexesWithOddEdges += 1
            if vertexesWithOddEdges > 2:
                return False
    return True

isEulerian = isEulerianPath(graph)
print(isEulerian)
