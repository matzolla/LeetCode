"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr=head
        
        if head==None: return head
        Next=head.next
        while Next!=None:
            
            if curr.val==Next.val:
                Next=Next.next
            else:
                curr.next=  Next
                curr=Next
                Next=Next.next
        curr.next=None
        
        
        return head
        