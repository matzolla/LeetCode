class Solution(object):
    def findKthPositive(self, arr, k):
        """
        
        :type arr: List[int]
        :type k: int
        :rtype: int

             [1,2,3,4,5,6,7,8,9,10,11]
        idx= [0,1,2,3,4]
        arr= [2,3,4,7,11]
        
        """
        for idx in range(len(arr)):

            x= arr[idx]-(idx+1)

            if x>=k:
                return idx+k
        else: return len(arr)+k
