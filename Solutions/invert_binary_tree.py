# Definition for a binary tree node.
# Time complexity O(N)
## space complexity O(1)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        ## recursive approach
        
        node=root
        
        if node!=None:
            
            left_node=node.left
            right_node=node.right
            
            ### swap nodes
            
            node.left=right_node
            node.right=left_node
            
            self.invertTree(node.left)
            self.invertTree(node.right)
            
        return root
