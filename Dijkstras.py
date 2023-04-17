import math
import random
#Goal: Write a program that randomly generates a graph that has a set amount of nodes and weighted edges
    # It'll print out a thing that shows the best and lowest weighted path to go through out the graph

"""dijkstraAlgo will take in the given graph and a source node. """

def dijkstraAlgo(Graph, source):
    maxHit = 3000
    allNodes = []
    smallDist = source
    visited_nodes = []
    for vert in Graph:
        math.dist[vert] = maxHit #initial distance from the source to vert is going the set to max
        previous[vert] = undef
        math.dist[source] = 0 #distance from the source ot the source
        allNodes.append(vert) #placing all of the nodes inside the loop
        while len(allNodes) == 0:
            u = allNodes.smallDist
            Q.remove(u)
            neighbors = vert.edges.node
            for neighbor in neighbors:
                if neighbor not in visited_nodes:
                    newDist = dist[u] + totalDistance #from the neighbor function (not yet defined)
                    if newDist < dist[neighbor]:
                        dist[neighbor] = newDist
                        previous[neighbor] = u
                        visited_nodes.append(neighbor)


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

    
def createGraph(numberNode):
    options = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    graph0 = Graph
    for i in range(numberNode):
        new_node = Node(options[i])
        graph0.add_node(new_node)
    for Node in graph0.nodes:
        number_edges = random.randint(1,4)
        for i in range(number_edges):
            random_node = graph0.nodes[random.randint(0,graph0.size)]
            Node.edges.append(random_node,random.randint(1,15))



        

class Node:
    def __init__(self,name):
        self.name = name
        self.edges = []
    def add_edge(self,node,weight):
        self.edges.append(node,weight)

class Graph:
    def __init__(self):
        self.nodes = []
        self.size = 0
    def add_node(self,Node):
        self.nodes.append(Node)
        self.size += 1
        
    