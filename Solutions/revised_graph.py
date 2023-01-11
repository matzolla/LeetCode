### Hey there we're revising graphs

## creating an adjacency matrix......

class graph:
    
    def __init__(self,edges):
        self.edges=edges

    ### create an adjacency matrix

    def adjacency(self):

        graph_matrix={}

        for a,b in self.edges:

            if a not in graph_matrix: 
                graph_matrix[a]=[]
            if b not in graph_matrix:
                graph_matrix[b]=[]

            ### append the edges
            graph_matrix[a].append(b)
            graph_matrix[b].append(a)

        return graph_matrix

    

    ### traversing a graph using bfs (this one only )


    def traverse_bfs(self,node):

        ## you're given the root

        queue=[node]
        traversal=[]

        graph_matrix=self.adjacency()

        while len(queue):
            curr = queue.pop(0)

            traversal.append(curr)

            for neigbours in graph_matrix[curr]:

                queue.append(neigbours)

        return traversal

    
    ### find path (recursive approach)

    def find_path(self,source,destination,seen):
        seen=set()
        graph_matrix=self.adjacency()
        if source in seen: return False
        if source==destination: return True

        seen.add(source)

        for neighbours in graph_matrix[source]:

            self.find_path(neighbours,destination,seen)



        return False

    ### connected components (solved)


    def count_components(self,node):
        seen=set()
        graph_matrix=self.adjacency()
        count=0
        for node in graph_matrix:

            if self.explore_node(node,seen)==True:

                count+=1

        return count

    def explore_node(self,node,seen):

        seen=set()
        graph_matrix=self.adjacency()
        if node in seen : return False

        seen.add(node)

        for neighbours in graph_matrix[node]:

            self.explore_node(neighbours,seen)


        return True

    
    def component_size(self,node):

        seen=set()
        graph_matrix=self.adjacency()
        max_size=-float('inf')

        for node in graph_matrix:

            value = self.explore_node_size(node,seen)


            if value> max_size:
                max_size=value

        return max_size


    def explore_node_size(self,node,seen):

        seen=set()
        count=1
        graph_matrix=self.adjacency()
        
        if node in seen(): return 0

        seen.add(node)

        for neighbours in graph_matrix[node]:
            count+=self.explore_node_size(neighbours,seen)


        return count



