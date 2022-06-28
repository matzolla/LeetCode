# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ### solving using BFS
        if root==None: return 0
        depth=0
        
        queue=[root]
        
        while len(queue)!=0:
            depth+=1
            
            for i in range(len(queue)):
                curr=queue.pop(0)
                if curr.left!=None: queue.append(curr.left)
                if curr.right!=None: queue.append(curr.right)
        
        return depth

### complexity analysis
## time complexity O(n)
## space complexity O(n) with n=number of nodes 