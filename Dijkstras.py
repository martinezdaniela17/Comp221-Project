import math
import random
#Goal: Write a program that randomly generates a graph that has a set amount of nodes and weighted edges
    # It'll print out a thing that shows the best and lowest weighted path to go through out the graph

"""dijkstraAlgo will take in the given graph and a source node. """

def dijkstraAlgo(Graph, source):
    maxHit = 3000 #Using a number we won't end up reaching
    allNodes = [] #Creating a list of all the nodes that'll be used and visited
    visited_nodes = []
    previous = {} #Variable to contain the previous node.
    dist = {} #Dictionary to store the distance to each node from the source
    for node in Graph:
        dist[node] = maxHit #initial distance from the source to node is set to maxHit
        previous[node] = None
        allNodes.append(node) #placing all of the nodes inside the loop
    dist[source] = 0 #distance from the source to the source is 0
    while allNodes: #This while loop's purpose is to remove the smallest distance between nodes from the allNodes list
        u = min(allNodes, key=lambda x: dist[x])
        allNodes.remove(u)
        neighbors = u.edges
        for neighbor, weight in neighbors:
            if neighbor not in visited_nodes: #If the neighbor isn't in the visited nodes, update the distance
                newDist = dist[u] + weight
                if newDist < dist[neighbor]: #If the newDist is less than the dist in neighbor, update the distance
                    dist[neighbor] = newDist
                    previous[neighbor] = u
        visited_nodes.append(u)
    return dist



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
def neighbor(node):
    neighbors = Null
    pair = [node, neighbors]
    vert = Null
    if node.edges.isempty() == False:
        vert = node
        totDist = math.dist(node, neighbor)
    else:
        #go to previous node
        pass


    
def createGraph(numberNode):
    options = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    graph0 = Graph
    for i in range(numberNode):
        new_node = Node(options[i]) ##ERROR STARTS HERE
        graph0.add_node(new_node)
    for Node in graph0.nodes:
        number_edges = random.randint(1,4)
        for i in range(number_edges):
            random_node = graph0.nodes[random.randint(0,graph0.size)]
            Node.edges.append(random_node,random.randint(1,15))
    return graph0



        

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
        
if __name__ == '__main__':
    graph_test = createGraph(5)
    node1 = graph_test.nodes[0]
    dijkstraAlgo(createGraph(5), node1)
    