class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        ## we can use countsort
        ## time complexity O(nlogn)

        ## but lets use sort here

        nums.sort()

        window_size=2

        result=0
        for idx in range(0,len(nums),2):

            result+=min(nums[idx:idx+window_size+1])
        
        return result
