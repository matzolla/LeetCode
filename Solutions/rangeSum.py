# Definition for a binary tree node.
# time complexity O(N)
# space complexity O(N)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        rangeSum=0
        if root==None: return rangeSum
        stack=[root]
        while len(stack):
            curr=stack.pop()

            if low<=curr.val<=high:
                rangeSum+=curr.val
            if curr.left!=None:
                stack.append(curr.left)
            if curr.right!=None:
                stack.append(curr.right)
        return rangeSum
