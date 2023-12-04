# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        [6,3,null,7,4,null,null,null,2,null,1,null,5]
        ## #make sure to understand the problem very well 
        ## this one was very tough !  got it right now the selected node should have left count, 
        right count or parent count greater so that we can win
        """
        hashset=set()
        powers=0
        
        for idx in range(10):
            powers+=2**idx
            
            if powers<=100:
                hashset.add(powers)
            
        # I have an idea 
        if x==1 and n in hashset: return False
        elif x==1 and n not in hashset: return True
        ## will do 2 dfs traversal algorithm
        
        ## first one to get the sub-tree containing the the value x of player 1
        
        stack1=[root]
        curr=root
        subtree=None
        
        while stack1 and curr.val!=x:
            curr=stack1.pop()
            if curr.val==x:subtree=curr
            if curr.right: stack1.append(curr.right)
            if curr.left: stack1.append(curr.left)
                
        ## now my second start is to count the node of the subtree
        
        stack2=[subtree]
        number_of_nodes=0
        left_count=0
        right_count=0
        while len(stack2):
            
            curr=stack2.pop()
            number_of_nodes+=1
            
            if curr.right: 
                stack2.append(curr.right)
                right_count+=1
            if curr.left: 
                stack2.append(curr.left)
                left_count+=1
        parent_count=n-(left_count+right_count+1)
        
        #if n - number_of_nodes < number_of_nodes: return False
        #else: return True
        if parent_count>(left_count+right_count) or right_count>(left_count+parent_count)or left_count>(parent_count+right_count): return True
        else:return False
