import math
#Goal: Write a program that randomly generates a graph that has a set amount of nodes and weighted edges
    # It'll print out a thing that shows the best and lowest weighted path to go through out the graph

def dijkstraAlgo():
    posInfinity = float('inf')
    for vert in Graph:
        math.dist[vert] = posInfinity
    print(posInfinity)

dijkstraAlgo
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