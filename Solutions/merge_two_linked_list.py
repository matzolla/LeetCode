# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        1 2 4 
        _
        1 3 4
        _
        
        1 1 2 4
        
        3 4
        a=1
        b=1
        if a==b
        
        if a<b
        
        if b<a
        
        """
        dummy=head=ListNode()
        
        while list1 and list2:
            
            if list1.val>list2.val:
                head.next=list2
                
                list2=list2.next
            else:
                head.next=list1
                list1=list1.next
            head=head.next
            
        if list1:
            head.next=list1
        if list2:
            head.next=list2
            
        return dummy.next

### time complexity O(n+m) where n= len(list1) and m=len(list2)
