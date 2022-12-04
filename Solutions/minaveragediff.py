class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        time complexity O(n) and space O(1)
        """
        
        prefix_sum=0
        
        total_sum=sum(nums)
        n=len(nums)
        value=float('inf')
        
        curr_index=0
        
        for idx,num in enumerate(nums):
            prefix_sum+=num
            idx+=1
            if idx!=n:
                curr_abs= abs((prefix_sum//idx)-((total_sum-prefix_sum)//(n-idx)))
            else:
                curr_abs= abs(prefix_sum//idx)
            if curr_abs<value:
                
                value=curr_abs
                
                curr_index=idx
        
        return curr_index-1
