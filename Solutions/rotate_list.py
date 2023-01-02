# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n=0
        count=0
        ##counting the number of nodes 
        node=head

        while node:
            node=node.next
            n+=1
        ### in case the rotation are greater we use the modulus

        if k<=0 or head==None or head.next==None:
            return head
        k=k%n
        ## now use two pointers

        if k==0: 
            return head
        fast=head
        
        while fast and count<k :

            fast=fast.next
            count+=1
        
        ### split the linked list
        Next=fast.next
        fast.next=None
        curr=Next
        
        while Next.next:
            Next=Next.next
        Next.next=head
        
        return curr
