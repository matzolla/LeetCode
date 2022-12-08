# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        [] 6 7 4 9 8
        """
        def leaf(root):

            stack=[root]
            nodes=[]

            while len(stack):
                curr=stack.pop()
                if curr.right!=None:
                    stack.append(curr.right)
                if curr.left!=None:
                    stack.append(curr.left)
                if curr.left==None and curr.right==None:
                    nodes.append(curr.val)
            return nodes
        leaves1=leaf(root1)
        leaves2=leaf(root2)
        return leaves1==leaves2
