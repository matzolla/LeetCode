class node():
    # traversing a linkedlist
    def __init__(self,val):
        self.val=val
        self.next=None

def printlinkedLIst(head):
    curr =head

    while curr!=None:

        print(curr)

        curr=curr.next

def recursivelinkedlist(head):
    curr=head
    if curr==None: return 0
    print(curr.val)

    return recursivelinkedlist(curr.next)
