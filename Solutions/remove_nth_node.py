# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next==None or head==None:
            return None
        
        curr= head
        Next=head
        
        for _ in range(n):
            Next=Next.next
        if Next==None:
            return head.next
        while Next.next!=None:
            
            curr=curr.next
            Next=Next.next
        remove_node=curr.next
        curr.next=remove_node.next
        
        return head

## space complexity O(1)
## time complexity O(n+ m) m= number of node traverse after n steps