# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        
        ## The idea is to traverse the tree using either bfs or dfs and append 
        ## the values of the array  time complexity will be O(nlogn)
        ## the hint require us to use the property of bst to optimize. Let's see
        ## using inorder traversal time complexity O(N), space O(N)
        
        stack=[root]
        curr=root
        nodes=[]
        while curr or len(stack)>1:
            
            while curr:
                stack.append(curr)
                curr=curr.left
                
            curr=stack.pop()
            nodes.append(curr.val)
            curr=curr.right
            
        return nodes[k-1]
# so we can use the bst inorder traversal to other nodes in an increasing order
