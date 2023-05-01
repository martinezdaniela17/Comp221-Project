import math
import random

class Node:
    def __init__(self, name):
        # Each node has a name and a list of edges
        self.name = name
        self.edges = []
    # Method to add an edge to the node
    def add_edge(self, node, weight):
        # An edge is a tuple of the neighbor node and its weight
        self.edges.append((node, weight))
    # This method returns the name of the node when it is printed
    def __repr__(self):
        return self.name
class Graph:
    def __init__(self):
        # A graph has a list of nodes and a size attribute
        self.nodes = []
        self.size = 0
    # Method to add a node to the graph
    def add_node(self,Node):
        # Add the node to the list of nodes and increment the size of the graph
        self.nodes.append(Node)
        self.size += 1
#Goal: Write a program that randomly generates a graph that has a set amount of nodes and weighted edges
    # It'll print out a thing that shows the best and lowest weighted path to go through out the graph

"""dijkstraAlgo will take in the given graph and a source node. """

def dijkstraAlgo(graph, source):
    maxHit = 1000 # Set a maximum value for distance
    # Initialize sets and dictionaries for visited nodes, previous nodes, and distances
    visited_nodes = []
    previous = {}
    dist = {}
    for node in graph.nodes: # Set the distance of each node to the source node to be the maximum value, and previous node to be none
        dist[node] = maxHit
        previous[node] = None
    dist[source] = 0 # Set the distance of the source node to be 0
    allNodes = set(graph.nodes) # Create a set of all nodes in the graph
    while len(graph.nodes) != 0: # Loop through the nodes until all have been visited
        u = min(graph.nodes, key=lambda x: dist[x])# Get the node with the smallest distance
        graph.nodes.remove(u) # Remove the node from the set of all nodes
        neighbors = u.edges # Get the neighbors of the node and their weights
        # Loop through the neighbors and update their distances and previous nodes if a shorter path is found
        for neighbor, weight in neighbors:
            newDist = dist[u] + weight
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                previous[neighbor] = u
            # Add the neighbor to the set of all nodes if it hasn't been visited yet
            if neighbor not in visited_nodes:
                graph.nodes.append(neighbor)
        visited_nodes.append(u) # Add the node to the set of visited nodes
    return dist # Return the dictionary of distances from the source node to all other nodes



def createGraph(numberNode):
    options = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Create a string of uppercase letters to use as node names
    graph0 = Graph() # Create an empty graph
    # Add nodes to the graph using the letter names
    for i in range(numberNode):
        new_node = Node(options[i])
        graph0.add_node(new_node)
        connected_nodes = set() # Keep track of nodes that have already been connected to other nodes
    for node in graph0.nodes:
        number_edges = random.randint(1, 4) # Choose a random number of edges to add to this node
        connected_nodes.add(node) # Add the current node to the set of connected nodes
        # Loop over the number of edges to add to this node
        for i in range(number_edges):
            unconnected_nodes = set(graph0.nodes) - connected_nodes # Find all nodes that have not yet been connected to the current node
            # If there are still unconnected nodes left, choose one at random
            if len(unconnected_nodes) > 0:
                random_node = random.sample(unconnected_nodes, 1)[0]
                node.add_edge(random_node, random.randint(1, 15)) # Add an edge between the current node and the randomly chosen node
                connected_nodes.add(random_node) # Add the randomly chosen node to the set of connected nodes
    return graph0 # Return the completed graph



if __name__ == '__main__':
    userInput = int(input("How many nodes would you like? Enter an integer between 2 and 26: "))
    while True:
        if 2 <= userInput <= 26: #If it's between 2 and 26, it'll be fine, else it'll ask again.
            graph_test = createGraph(userInput) #Allows the user to add the amount of nodes they want
            node1 = graph_test.nodes[0]
            print(dijkstraAlgo(graph_test, node1))
            break
        else:
            userInput = int(input("How many nodes would you like? Enter an integer between 2 and 26: "))