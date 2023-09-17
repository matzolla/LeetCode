class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int

        
        example: [1,2,3,4,5,6,7,8,9,10,11]
        
        time complexity O(n)
        space complexity O(1)
        """

        for idx in range(len(arr)):

            x= arr[idx]-(1+idx)

            if x>=k:
                return idx+k

        return len(arr)+k
