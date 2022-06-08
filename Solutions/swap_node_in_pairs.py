"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example : Input: 1--->2--->4--->3
        Output: 2--->1--->3--->4
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution(object):
    def swap_node(self, nodes):

        # Input : [linked list of nodes]
        # Output : [nodes swapt]


        while (nodes!=None) and (nodes.next!= None):

            ## collect val

            curr_node_val=nodes.val
            next_node_val=nodes.next.val

            ## swap values

            nodes.val=next_node_val
            nodes.next.val=curr_node_val
        
        return nodes