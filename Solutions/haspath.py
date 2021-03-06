"""
Here we write an algorithm to check if a graph has path from source node 
to destination node. We suppose we're in a directed acyclic grpah
"""

class solution(object):

    def haspath(self,graph,src,dst):

        # graph is an adjacency list of nodes
        # src is the source nodes
        # dst is the destination node

        ## using dfs

        stack=[src] # initialize the stack with a source node

        ## current node 

        
        while stack!=None:

            curr=stack.pop()

            if curr==dst: return True
            else:
                for nodes in graph[curr]:

                    stack.append(nodes)
        ### if hasn't find root  then return False

        return False


### complexity analysis, time complexity O(e) e= number of edges

### space complexity O(N) N = number of nodes
