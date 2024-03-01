class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        jump=0
        
        for i in range(len(nums)):
            if jump< i : return False ### meaning we can't jump
            
            jump= max(jump,i+nums[i])
            
        return True
   
  
  # Space complexity O(1)
  # time O(n)
