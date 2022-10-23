# Definition for a binary tree node.
# Sample solution
"""a simple way:
         
         if not p and not q: return True
         if not p or not q: return False
         if p.val!=q.val: return False
         
         return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)"""
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
        """
        ### sanity checking

        if p==None and q!=None: return False
        if p!=None and q==None: return False
        if p==None and q==None: return True
        stack_p=[(p,p.val)]
        stack_q=[(q,q.val)]
        
        ## normaly both tree should be thesame both in number and properties
        while len(stack_p)>0 and len(stack_q)>0:
            curr_p,val_p=stack_p.pop()
            curr_q,val_q=stack_q.pop()
            
            if val_p!=val_q: return False
            ## check for similarity
            if curr_p.right and curr_q.right:
                stack_p.append((curr_p.right,curr_p.right.val))
                stack_q.append((curr_q.right,curr_q.right.val))
            if (curr_p.right==None and curr_q.right!=None)or (curr_p.right!=None and curr_q.right==None):
                return False
            
            if curr_p.left and curr_q.left:
                stack_p.append((curr_p.left,curr_p.left.val))
                stack_q.append((curr_q.left,curr_q.left.val))
            if (curr_p.left==None and curr_q.left!=None) or (curr_p.left!=None and curr_q.left==None):
                return False
            if (curr_p.left==None and curr_q.left==None)and(curr_p.right==None and curr_q.right==None): return True
        
        
        return False
