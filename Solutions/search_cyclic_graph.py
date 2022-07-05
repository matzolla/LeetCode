"""
here we're searching in a directed cyclic graph so we
should overcome the challenge of infinite loops when 
traversing the graph

"""


def solution(graph,src,dst):

    # graph: we have the graph
    # src the source node 
    # dst: the destination node
    # visited a set that defines if a node is visited or not 

    visited= set()
    if src==dst: return True

    if src in set: return False

    visited.add(src)

    for curr in graph[src]:

        if solution(graph,curr,dst,visited)==True:
            return True 
    


    return False


