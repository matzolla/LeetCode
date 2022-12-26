class bubble_sort:

    """
    A=[5,0,7,10,2]
    A= [5,0,7,2,10]
    [5,0,2,7,10]
    [0,5,2,7,10]

    Time complexity O(n^2)
    space complexity O(1)

    """

    def __init__(self,array):
        self.arr=array
    
    def sort(self):

        right=len(self.arr)-1

        for idx in range(right):

            for idy in range(right,idx,-1):

                if self.arr[idy-1]>self.arr[idy]:
                    self.arr[idy-1],self.arr[idy]=self.arr[idy],self.arr[idy-1]

array=[5,0,7,10,2]
sorting=bubble_sort(array)

sorting.sort()


print(array)
