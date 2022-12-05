# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
         time complexity O(N), space complexity O(1)
         
         but two pointer is better slow pointer= head
                                   fast pointer = head
                                    
                                   while slow and fast.next
                                       slow=slow.next
                                       fast=fast.next.next
                                   return slow
        """
        num_nodes=0
        idx=1
        curr,node=head,head
        
        while curr:
            num_nodes+=1
            curr=curr.next
        
        num_nodes//=2 
        
        while idx<=num_nodes:
            
            node=node.next
            idx+=1
        
        return node
