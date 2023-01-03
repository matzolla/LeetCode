# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        
        passed 58/60 test cases 
        time complexity O(max(P,Q)), space O(max(p,q))
        
         I came to the conclusion that, I don't necessarily need dfs or bfs to 
         solve all binary tree problems
         
         
         
         a simple way:
         
         if not p and not q: return True
         if not p or not q: return False
         if p.val!=q.val: return False
         
         return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        """
        ### sanity checking

        if not p and not q: return True
        if not p or not q: return False
        if p.val!=q.val: return False

        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
