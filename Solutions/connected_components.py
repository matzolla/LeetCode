"""
here we want to use the idea of connected components 
to solve problems related to directed cyclic graph
"""

def connected_components(graph):
    # the graph structure algorithm
    # src: the source node 
    count=0
    visited = set()

    for nodes in graph:
        if explore(graph,nodes, visited)==True:
            count+=1
        
    return count ### this can be used to solve the island problem



def explore(graph,node,visited):

    if node in visited: return False

    visited.add(node)

    for neighbours in graph[node]:

        explore(graph,neighbours,visited)

    return True



## time complexity O(e) : e been the number of edges
## space complexity O(N): N the number of nodes

    




    
