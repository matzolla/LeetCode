class solution(object):

    def haspath(self,graph,src,dst):
        
        # src is the source nodes
        # dst is the destination node

        # using dfs

        stack=[src] 
        # initialize the stack with a source node

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
