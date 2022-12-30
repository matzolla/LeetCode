class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        idea using dynamic sliding windows 
        time complexity of the other of O(n^3)
        space complexity of O(1) so far
        
        
        can further improve the time complexity to
        
        O(N) as well as space of O(1) :
        learned something new
        
        """
        min_product=nums[0]
        max_product=nums[0]
        Max=nums[0]
        for idx in range(1,(len(nums))):
            
            min_product,max_product=min(min_product*nums[idx],nums[idx],max_product*nums[idx]),max(max_product*nums[idx],nums[idx],min_product*nums[idx])
            

            Max=max(Max,max_product)

        return Max
