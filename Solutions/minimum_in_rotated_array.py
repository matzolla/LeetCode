class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        
        if len(nums)==1:
            
            return nums[0]
        
        while left<right:
            middle=(right+left)//2
            
            if nums[middle]<nums[right]:
                right=middle
            else:
                left=middle+1
            
        return nums[left]
## time complexity O(logn) 
## space complexity O(1)
