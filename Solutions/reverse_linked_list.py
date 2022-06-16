"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
## Example 1-->2-->3-->4-->None     output: 4-->3-->2-->1-->None


class solution(object):

    def reverse_linked_list(self,head):
        # Input : head of a linked list
        # Output : reverse link list

        ## previous node

        previous_node=None
        ## current node
        curr=head


        while curr!=None:
            ##next node

            next=curr.next

            ## next becomes previous

            curr.next=previous_node

            ## swap current with previous

            previous_node=curr

            ## current node become next

            curr=next

        return previous_node      
        
## the reason why I say previous node because is because the previous node is the last none  zero node

## complexity analysis

## time complexity O(N) with N = len(linklist)
## Space complexity O(1)




