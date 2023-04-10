import math
#Goal: Write a program that randomly generates a graph that has a set amount of nodes and weighted edges
    # It'll print out a thing that shows the best and lowest weighted path to go through out the graph

def dijkstraAlgo(Graph, source):
    maxHit = 3000
    allNodes = []
    smallDist = source
    for vert in Graph:
        math.dist[vert] = maxHit #initial distance from the source to vert is going the set to max
        previous[vert] = undef
        math.dist[source] = 0 #distance from the source ot the source
        allNodes.append(vert) #placing all of the nodes inside the loop
        

    

# 2:	for each vertex v in Graph:	// Initialization
# 3:	dist[v] := infinity	// initial distance from source to vertex v is set to infinite
# 4:	previous[v] := undefined	// Previous node in optimal path from source
# 5:	dist[source] := 0	// Distance from source to source
# 6:	Q := the set of all nodes in Graph	// all nodes in the graph are unoptimized - thus are in Q
# 7:	while Q is not empty:	// main loop
# 8:	u := node in Q with smallest dist[ ]
# 9:	remove u from Q
# 10:	for each neighbor v of u:	// where v has not yet been removed from Q.
# 11:	alt := dist[u] + dist_between(u, v)
# 12:	if alt < dist[v]	// Relax (u,v)
# 13:	dist[v] := alt
# 14:	previous[v] := u

class Node:
    def __init__(self,name):
        self.name = name
        self.edges = []
    def add_edge(self,node,weight):
        self.edges.append(node,weight)