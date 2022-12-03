# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        Time complexity O(n)
        Space complexity O(n)
        """
        stack=[root]
        curr=root
        nodes=[]
        while (curr or len(stack)>1):
            while curr:
                stack.append(curr)
                curr=curr.left
                
            curr=stack.pop()
            nodes.append(curr.val)
            curr=curr.right
        
        return nodes
  
