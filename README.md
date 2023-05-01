# Comp221-Project

The purpose of this project is to implement Dijktra's algorithm and to return the weight to get to each. In "Dijkstras.py" we build the entire algorithm and "playingWDijkstras.py" we attempt to make the visual of the graph.

# DIJKSTRAS:

The purpose of Dijkstra is to return the lightest weighted path around a graph. The Dijkstra file contains 2 classes, Node and Graph. 

The Node class contains three functions to assign a name in a list of edges, adding an edge, and returning names. These are used throughout the program.

The Graph Class contains 2 functions used to store the nodes in a list and adding nodes to the graph.

dijkstraAlgo takes in two parameters, graph and source, in which graph contains all the nodes and the source will be the initial node. This function will be able to store all of the nodes so we can later visit and measure the general weight of paths.

createGraph takes in one node, numberNode, which is meant to be inputted by the user. The purpose of this function is to assign random values to the weight of the edges and adding the nodes to the graph.  Once this goes through all the nodes and edges assigned to the node, it will return the graph.

We allow the user to input an ammount of nodes within the values of 2 through 26. What will be returned will be the weight of the paths between the nodes.

# playingWDijsktras

This one has the same functionality but with the attempts of making the visual graph using networks.

# LINKS WE USED:

Link to help us visualize dijkstra: 
https://stackoverflow.com/questions/48103119/drawing-a-network-with-nodes-and-edges-in-python3
https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259
https://pyvis.readthedocs.io/en/latest/index.html

Link to help with graph stuff: https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.has_edge.html

Link for general implementation: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

