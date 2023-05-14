"""
Here we're creating a dfs algorithm for binary tree
As usual, we're using a stack for dfs and queue for bfs
"""

class Tree(object):

    def __init__(self,val=0,left=None,right=None):

        self.left=None
        self.right=None
        self.val=0

class dfs(object):

    def solution(self,root):

        if root ==NULL: return []
        result=[]
        stack=[root]


        while len(stack)!=0:

            curr=stack.pop()

            result.append(curr.left)
            result.append(curr.right)

        return result

        
