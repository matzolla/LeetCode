class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """[0,0,1,1,1,2,2,3,3,4]
         _   _ 
           _  """
        left=0
        right=1
        idx=1
            
        while (left<len(nums))and(right<len(nums))and idx<=len(set(nums)):
            if nums[left]==nums[right]:
                right+=1
            else:
                nums[idx]=nums[right]
                left=right
                right+=1
                idx+=1
                print(idx)
        return len(set(nums))
 # time complexity O(n) inplace. test case 360/361
