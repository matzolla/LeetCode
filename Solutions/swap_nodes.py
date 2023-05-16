# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        values=[]
        curr=head

        while curr:
            values.append(curr.val)
            curr=curr.next

        values[k-1],values[len(values)-k]= values[len(values)-k],values[k-1]

        dummyhead= ListNode()
        node=dummyhead
        for val in values:

            node.next= ListNode(val)
            node=node.next

        return dummyhead.next
