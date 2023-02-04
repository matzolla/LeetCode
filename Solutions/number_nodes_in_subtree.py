class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]

        i have a brute force approach
        we iterate through each node and check if the condition holds
        
        time complexity O(n^2)
        
        not fully optimal
        """

        if n==1: return [1]
        result=[]
        matrix={}    
        for a,b in edges:
            if a not in matrix:
               matrix[a]=[]
               
            if b not in matrix:
                matrix[b]=[]

            matrix[a].append(b)
            matrix[b].append(a)
        nodes= list(matrix.keys())


        ## now let's do the dfs algorithm
        seen =set()
        for node in nodes:

            local_seen=set()
            stack=[node]
            count=0
            while len(stack):
                
                curr=stack.pop()
                if curr in seen:
                    continue
                if (curr in local_seen):
                    continue
                local_seen.add(curr)
                if labels[curr]==labels[node]:
                    count+=1
                for neigh in matrix[curr]:

                    stack.append(neigh)
            seen.add(node)
            result.append(count)
        return result
