# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack =[(root,float('inf'),-float('inf'))]
        
        while len(stack)>0:
            
            curr,_max,_min=stack.pop()
            if curr.val>=_max or curr.val<=_min:
                return False
            if curr.right:
                stack.append((curr.right,_max,max(_min,curr.val)))
            if curr.left:
                stack.append((curr.left,min(_max,curr.val),_min))
        return True
 
        # Time complexity O(N)
        # space complexity O(h)
