class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum=0
        largest_sum=-float('inf')
        
        if len(nums)==1: return nums[0]
        
        for i in range(len(nums)):
            
            curr_sum=max(curr_sum+nums[i],nums[i])
            
            if curr_sum>largest_sum:
                largest_sum=curr_sum
            
        return largest_sum
      
# time complexity O(n), space complexity O(1)
