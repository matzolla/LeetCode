class quick_sort_algo:

    ### worst case o(n^2)
    ### best case o(nlogn)

    def __init__(self,array):
        self.array=array
    
    def partition(self,p,r):

        x=self.array[r]

        idx=p-1
        idy=p
        while idy <= r-1:

            if self.array[idy]<=x:

                idx+=1

                self.array[idx],self.array[idy]=self.array[idy],self.array[idx]

                idy+=1
        self.array[idx+1],self.array[r]= self.array[r],self.array[idx+1]


        return idx+1
        




    def quick_sort(self,p,r):
        
        if p<r:

            q=self.partition(p,r)

            self.quick_sort(p,q-1)

            self.quick_sort(q+1,r)
        