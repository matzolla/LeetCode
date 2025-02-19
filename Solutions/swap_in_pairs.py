## Definition for singly-linked list.
## time complexity O(N), space complexity O(1)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummylist= ListNode()
        ## attaching the head to the dummylist
        dummylist.next=head
        prevnode=dummylist
        currnode=head

        while currnode and currnode.next:
            prevnode.next=currnode.next
            currnode.next=prevnode.next.next
            prevnode.next.next=currnode

            prevnode=currnode

            currnode=currnode.next

        return dummylist.next
