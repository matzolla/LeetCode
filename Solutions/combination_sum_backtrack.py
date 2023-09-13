## backtrack
class comb():
    def __init__(self,candidate,target):
        self.candidate=candidate
        self.target=target
        self.curr_comb=[]
        self.result=[]
        self.curr_sum=0
    
    def combination_sum(self):
        self.comb_sum(0)

        return self.result
        
    def comb_sum(self,currindex):
        if self.curr_sum>self.target: return 
        if self.curr_sum==self.target:
            self.result.append(list(self.curr_comb))

            return  

        for idy in range(currindex,len(self.candidate)):

            self.curr_sum+=self.candidate[idy]

            self.curr_comb.append(self.candidate[idy])

            self.comb_sum(idy)
            self.curr_comb.pop()

            self.curr_sum-=self.candidate[idy]


candidate=[2,3,6,7]
target=7
print(comb(candidate,target).combination_sum())
# you can ignore the coding example below
# as it is related to heap data structure
arr=[3,2,4,9,6]
import heapq

heapq.heapify(arr)

k=3
while len(arr)>=k:

    curr=heapq.heappop(arr)
    print(curr)
####### generating paranthesis ###########
