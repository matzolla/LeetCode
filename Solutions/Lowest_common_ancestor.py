class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        using bfs
        [(2,5,2),(6,5,2),(4,2,3),(7,2,3)] (3,3,0) (1,3,1) (5,3,1) (0,1,2),(8,1,2)
        ancestor=1
        """
        depth=0
        queue=[(root,root,depth)]
        levels=collections.defaultdict(list)
        ancestors=dict()
        while len(queue):

            node,ancestor,height=queue.pop(0)
            ancestors[node]=ancestor
            levels[height].append(node)
            if node.right:
                queue.append((node.right,node,height+1))
            if node.left:
                queue.append((node.left,node,height+1))
            
        deepest=levels[len(levels)-1]

        ## check if deepest containes only one node
        if len(deepest)==1: return deepest[0]

        ## otherwise get the parents of the deepest nodes

        while True:

            deepest=[ancestors[node] for node in deepest ]
            if len(set(deepest))==1:
                return deepest[0]

        #return lowest_ancestor
# Definition for a binary tree node.
