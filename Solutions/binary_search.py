
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""
## nums = [-1,0,3,5,9,12], target = 9

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        
        right=len(nums)-1
        
        while (left<=right):
            
            middle= (right+left)//2
            
            if nums[middle]==target: return middle
            
            if nums[middle]< target:
                
                left=middle+1
            else:
                right=middle-1
        return -1

### complexity analysis 

## time O(logn)
## space O(n)