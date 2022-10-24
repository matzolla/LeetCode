class MergeSort:

    def __init__(self,array):
        self.array=array

    def merge(self,p,q):

        idx=0

        idy=0

        idz=0
        ## sorted elements will be stored 
        ## in the array sorted
        sorted=[0]*len(self.array)

        ### defining the lower and upper bound 
        ## of the array
        q=len(self.array)
        p=0

        r=(p+q)//2

        ### subdivide the array into smaller tasks
        # Creating the left and right array 
        left_array= self.array[p:r+1]

        right_array=self.array[r:q]


        while idx< len(left_array) and idy<len(right_array):

            if left_array[idx]<= right_array[idy]:
                sorted[idx]=left_array[idx]

                idx+=1
            else:
                sorted[idy]=right_array[idy]
                idy+=1

            idz+=1

       ## if some elements still remains, then append it 
        while idx< len(left_array):
            sorted[idx]=left_array[idx]

            idx+=1
            idz+=1

      ## do thesame for the right array
        while idy< len(right_array):
            sorted[idy]=right_array[idy]

            idy+=1
            idz+=1


       ## time complexity O(nlogn)
       ## space complexity O(n+m)

        return sorted








