"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Example:
   (1)
   /\
  /  \
(2)   (3)  target:5

output: False
"""
########difficulty : Easy###############
## defining a class
from tkinter import N


class TreeNode(object):
     def __init__(self,val=0,left=None,right=None):
         self.val=val
         self.left=left
         self.right-right

class Solutions(object):
    def haspath(root,target):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        result=0

        ## instanciate an empty set

        nodes=set()
        residu=[None]
        while (root!=None) and(result!=target)and(root.val!=0):
            if root not in nodes:        ###time complexity of O(1) for ordered set
                result+=root.val 
                nodes.add(root)
                residu.append(root)     #### time complexity
            else:
                continue

            if result<target:
                if (root.left!=None)and(root.left.val!=0): root=root.left
                elif (root.right!=None)and(root.right.val!=0): root=root.right
                else:
                    node=residu.pop()   ## remove out the node
                    root=residu[-1]     ## taking the one before the last
                    result-=node.val    ##  reduce the result 
                    node.val=0          ## mark the node as passed by replacing by 0
            else:
                node=residu.pop()   
                root=residu[-1]     
                result-=node.val 
                node.val=0 
        
        return result==target


####Complexity analysis ###########

##best case scenario time complexity will be O(len(residu))
## worst case scenario (No solution) time complexity will be O(len(Graph))

## space complexity O(len(nodes)+len(residus))---->linear

                    

