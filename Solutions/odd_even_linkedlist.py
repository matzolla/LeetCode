# Definition for singly-linked list.
## time complexity O(N), space O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head==None: return 
        even,evenhead=head.next,head.next
        odd=head

        while even and even.next:
            odd.next=even.next
            odd=odd.next

            even.next=odd.next
            even=even.next

        odd.next=evenhead

        return head
