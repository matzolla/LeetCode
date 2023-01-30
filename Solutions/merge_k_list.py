class Linklist:

    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class merge_k_list:

    def __init__(self,linkedlist):

        self.linkedlist=linkedlist


    def merge_k(self):

        merged_list=[]

        while len(self.linkedlist)>1:

            for idx in range(0, len(self.linkedlist),2):

                list1= self.linkedlist[idx]

                list2=self.linkedlist[idx+1] if (idx+1< len(self.linkedlist)) else None

                merged_list.append(self.merged(list1,list2))


            self.linkedlist= merged_list


        
        return self.linkedlist
    
    def merge(self,list1,list2):

        dummy=Linklist(0)

        curr=dummy

        while list1 and list2:

            if list1.val< list2.val:

                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next

        if list1:
            curr.next=list1

        if list2:
            curr.next=list2

        return dummy.next


# Question, can we solve it using heap priority queue?
# 
#
#
#