class my_heap:

    def __init__(self):
        self.array=None

    def parent(self,idx):
        return idx//2

    def left_child(self,idx):
        return 2*idx

    def right_child(self,idx):
        return 2*idx+1

    def heapify(self,array,idx):
        largest=idx

        left= self.left_child(idx)
        right=self.right_child(idx)


        if left <= len(array)-1 and array[left]> array[idx]:
            largest=left
        else: largest=idx


        if right <= len(array)-1 and array[right]> array[largest]:
            largest=right
        if largest!=idx:
            array[largest],array[idx]= array[idx],array[largest]


        return self.heapify(array,largest)

    

    def max_heap(self,array):

        for idy in range ((len(array)//2)-1,-1,-1):

            self.heapify(idy)

    def heapsort(self,array):
        ### initialize the length of the heap
        ### swap the first and last value of the heap.
        ## decrement the size of the heap by 1 
        ## heapify the updated heap
        ## continue till convergence :)

        n= len(array)-1

        while n>=0:
            array[0],array[n]=array[n],array[0]
            n-=1
            self.heapify(array[:n],idx=0)
            


    ##### Implementing the priority queue

    #1) return max 

    def get_max(self,array):
        ## return the max of the heap
        return array[0]

    def extract_max(self,array):
        n=len(array)-1
        max_=array[0]

        ## swap first and last node

        array[0],array[n]=array[n],array[0]
        n-=1
        self.heapify(array[:n],0)

        return max_

    def insert_key(self,array,idx,value):

        if value< array[idx]:
            raise "new value is less than current value"

        else:
            array[idx]=value
            parent=self.parent(idx)
            while idx >0 and array[parent]< array[idx]:
                ### swap nodes

                array[parent],array[idx]=array[idx],array[parent]

                parent=self.parent(parent)

    def update_key(self,array,value):

        n=len(array)
        array[n]=-float('inf')

        self.insert_key(array,n,value)

        


            