# Comp221-Project

Link to help us visualize dijkstra: https://stackoverflow.com/questions/48103119/drawing-a-network-with-nodes-and-edges-in-python3

Link to help with graph stuff: https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.has_edge.html

Link for general implementation: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

Pesudocode:
function Dijkstra(Graph, source):
2:	for each vertex v in Graph:	// Initialization
3:	    dist[v] := infinity	// initial distance from source to vertex is set to infinite
        previous[v] := undefined	// Previous node in optimal path from source
5:	dist[source] := 0	// Distance from source to source
6:	Q := the set of all nodes in Graph	// all nodes in the graph are unoptimized - thus are in Q
7:	while Q is not empty:	// main loop
8:	    u := node in Q with smallest dist[ ]
9:	    remove u from Q
10:	    for each neighbor v of u:	// where v has not yet been removed from Q.
11:	        alt := dist[u] + dist_between(u, v)
12:	        if alt < dist[v]	// Relax (u,v)
13:	            dist[v] := alt
14:	            previous[v] := u
15:	    return previous[ ]


#create function for neighbhors of node, take in Node and Edges (2 params)
    #create neighbors = null
    #pair = [Node, neighbors]
    #if node has edges
        # check to see nodes connected to edge 
        # set vertex to node
        #if pair has been visted
            #change neighbor to another
        #total distance = dist(Node, neighbor)
    #else if node has no edges
        # go back one node
    #return total distance

#Delete it if it's not necessary
# def neighbor(node):
#     neighbors = Null;
#     pair = [node, neighbors]
#     vert = Null;
#     if node.edges.isempty() == False:
#         vert = node
#         totDist = math.dist(node, neighbor)
#     else:
#         #go to previous node
#         pass
