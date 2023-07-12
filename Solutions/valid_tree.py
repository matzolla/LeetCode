def  adjacency(edges):
        
        ## runtime complexity O(m+e)
        ## space complexity O(e) number of nodes

        graph={}
        for edge in edges:
             a,b =edge             
             graph[a]= b
             graph[b] =a


       Return graph

def  is_valid_Tree(graph, root):
       stack= [root]
       Seen = set()
       While len(stack):
             curr= stack.pop()
             
             if curr is in Seen:
                   Return False
             Seen.add(curr)
             for  neighbour in graph[curr]:
                    stack.append(neighbour)
         if len(Seen) < n : return False
      Return True
