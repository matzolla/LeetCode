# Definition for singly-linked list.
class ListNode(object):
    # class to define a linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead=ListNode()
        curr=dummyHead
        carry=0

        while l1 and l2:
            value= l1.val + l2.val + carry

            carry=value%10

            curr.next=ListNode(carry)
            carry=value//10
            l1=l1.next
            l2=l2.next
            curr=curr.next
        
        while l1:
            value=l1.val+ carry
            carry=value%10
            curr.next=ListNode(carry)
            carry=value//10
            l1=l1.next
            curr=curr.next
        
        while l2:
            value=l2.val+ carry
            carry=value%10
            curr.next=ListNode(carry)
            carry=value//10
            l2=l2.next
            curr=curr.next
        if carry!=0:
            curr.next=ListNode(carry)

        return dummyHead.next
