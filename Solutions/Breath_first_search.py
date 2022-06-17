"""We are given a directed graph, and we want to return the list of

it's traversal using BFS"""

##Example

#  graph={
#         a:['c','b'],
#         b: ['d'],
#         c:  ['e'],
#         d:  ['f'],
#         e:  [],
#         f:  []
#        }


## Output: ['a','b','d','f','c','e']





class solution(object):

    def BFS(self,graph,source):
        # Input graph and source node
        # output: BFS traversal
        #

        queue= [source]

        #output list
        output=[]

        while queue!=None:

            ## current node

            curr=queue.pop(0)

            output.append(curr)

            for nodes in graph[curr]:

                ### nodes in graph

                queue.append(nodes)

        

        return output