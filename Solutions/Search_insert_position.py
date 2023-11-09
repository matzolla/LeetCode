class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## time complexity O(logn)
        ## space complexity O(1)
        left = 0
        right=len(nums)-1

        while left<=right:

            mid= (left+right)//2

            if nums[mid]==target: return mid

            if nums[mid]>target:
                right=mid-1
            else:
                left=mid+1

        return mid+1 if target>nums[mid] else mid
        
