# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        
     the solution requires an auxilary space complexity of O(N)
        """
        
        stack=[]
        curr=head
        
        while curr:
            stack.append(curr)
            curr=curr.next
            
            
        ### next step
        left=0
        right=len(stack)-1
        for idx in range(len(stack)):
            
            if idx%2==0:
                
                head.next= stack[left]
                
                left+=1
            else:
                head.next=stack[right]
                right-=1
            head=head.next
        head.next=None
 ## linear time complexity O(N)
            
