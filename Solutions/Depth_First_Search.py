"""We are given a directed graph, and we want to return the list of

it's traversal using DFS"""

##Example

#  graph={
#         a:['c','b'],
#         b: ['d'],
#         c:  ['e'],
#         d:  ['f'],
#         e:  [],
#         f:  []
#        }
## 


## Output: ['a','b','d','f','c','e']

class solution(object):
    
    def dfs(self,graph,source):

        ### initialize a stack with source node

        stack=[source]

        output=[]

        while stack !=None:

            ## current node = node in stack

            curr= stack.pop()

            output.append(curr)

            for nodes in graph[curr]:

                stack.append(nodes)
        

        return output

### complexity analysis: 

## Time O(N) with N= len(grapg)
## Space complexity O(1)
