## backtracking [1,2,3]=[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
# time complexity O(2^n)
# space complexoty O(space)\


class permutation:

    def __init__(self,array):

        self.result=[]
        self.array=array
        self.n=len(self.array)
        
    def permute_array(self,index):

        if index== self.n:
            self.result.append(list(self.array)) 

            print(self.result)


        for idy in range(index,self.n):

            self.array[index],self.array[idy]=self.array[idy],self.array[index]


            ### backtrack

            self.permute_array(index+1)

            self.array[index],self.array[idy]=self.array[idy],self.array[index]
