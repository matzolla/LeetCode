"""
Checking if a binary tree has a path to a destination or not
"""

class Tree(object):

    def __init__(self,left,right,val):
        self.left=None
        self.right=None
        self.val=0

class solution(object):

    def haspath(self,root,dst):

        stack=[root]

        while len(stack)!=0:
            curr= stack.pop()

            if curr==dst: return True

            if curr.right!=None:stack.append(curr.right)

            if curr.left!=None: stack.append(curr.left)
        

        return False