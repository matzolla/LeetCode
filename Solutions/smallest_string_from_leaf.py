"""
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        ## just for test :)
        nums=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18",
             "19","20","21","22","23","24","25"]
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
             "s","t","u","v","w","x","y","z"]
        hash_num=dict.fromkeys(nums,0)
        
        ## initialize hash
        for  num,alph in zip(nums,alphabet):
            hash_num[num]=alph

            

        stack=[(root,hash_num[str(root.val)])]
        nodes=[]
        leaf=[]
        ### is leaf function
        def isleaf(node):
            if (node.left==None and node.right==None):
                return True
            else:
                return False
            
        ## depth-first-search
        while len(stack)!=0:
            node,char=stack.pop()
            nodes.append((node,char))
            if node.left: stack.append((node.left,char+hash_num[str(node.left.val)]))
            if node.right: stack.append((node.right,char+hash_num[str(node.right.val)]))
        ## check who is leaf
        
        for content in nodes:
            
            node,string= content
            
            if isleaf(node):
                leaf.append(string[::-1])

        leaf.sort()
        
        return leaf[0]


### time complexity O(n+nlogn)
### space complexity O(n+m)
## n= len(nodes), m=len(leaf)



            