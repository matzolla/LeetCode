# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root==None:
            return False
        def is_leaf(node):
            
            return node.left==None and node.right==None
        
        queue=[(root,root.val)]
        
        while len(queue)!=0:
            
            curr,value=queue.pop(0)
            if is_leaf(curr):
                
                if targetSum==value:
                    
                    return True
            if curr.left!=None:
                curr.left.val+=value
                queue.append((curr.left,curr.left.val))
            if curr.right!=None:
                curr.right.val+=value
                queue.append((curr.right,curr.right.val))
                
        return False 
      ## Time complexity O(n)
      ## Space complexity O(n)
