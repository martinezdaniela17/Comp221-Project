import math
import random

# Node class represents a node in the graph
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
# Graph class represents a graph
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
    # Set a maximum value for distance
    maxHit = 3000
    # Initialize sets and dictionaries for visited nodes, previous nodes, and distances
    visited_nodes = set()
    previous = {}
    dist = {}
    # Set the distance of each node to the source node to be the maximum value, and previous node to be none
    for node in graph.nodes:
        dist[node] = maxHit
        previous[node] = None
    # Set the distance of the source node to be 0
    dist[source] = 0
    # Create a set of all nodes in the graph
    allNodes = set(graph.nodes)
    # Loop through the nodes until all have been visited
    while allNodes:
        # Get the node with the smallest distance
        u = min(allNodes, key=lambda x: dist[x])
        # Remove the node from the set of all nodes
        allNodes.remove(u)
        # Get the neighbors of the node and their weights
        neighbors = u.edges
        # Loop through the neighbors and update their distances and previous nodes if a shorter path is found
        for neighbor, weight in neighbors:
            newDist = dist[u] + weight
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                previous[neighbor] = u
            # Add the neighbor to the set of all nodes if it hasn't been visited yet
            if neighbor not in visited_nodes:
                allNodes.add(neighbor)
        # Add the node to the set of visited nodes
        visited_nodes.add(u)
    # Return the dictionary of distances from the source node to all other nodes
    return dist



def createGraph(numberNode):
    # Create a string of uppercase letters to use as node names
    options = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Create an empty graph
    graph0 = Graph()
    # Add nodes to the graph using the letter names
    for i in range(numberNode):
        new_node = Node(options[i])
        graph0.add_node(new_node)
    # Keep track of nodes that have already been connected to other nodes
    connected_nodes = set()
    for node in graph0.nodes:
        # Choose a random number of edges to add to this node (between 1 and 4)
        number_edges = random.randint(1, 4)
        # Add the current node to the set of connected nodes
        connected_nodes.add(node)
        # Loop over the number of edges to add to this node
        for i in range(number_edges):
            # Find all nodes that have not yet been connected to the current node
            unconnected_nodes = set(graph0.nodes) - connected_nodes
            # If there are still unconnected nodes left, choose one at random
            if len(unconnected_nodes) > 0:
                random_node = random.sample(unconnected_nodes, 1)[0]
                # Add an edge between the current node and the randomly chosen node,
                # with a random weight between 1 and 15
                node.add_edge(random_node, random.randint(1, 15))
                # Add the randomly chosen node to the set of connected nodes
                connected_nodes.add(random_node)
    # Return the completed graph
    return graph0



if __name__ == '__main__':
    graph_test = createGraph(5)
    node1 = graph_test.nodes[0]
    print(dijkstraAlgo(graph_test, node1))
    