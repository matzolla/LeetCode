class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        brute force of O(n^3) i've optimized to O(n^2)
        but i think can be optimized to o(nlogn)
        [-4,-1,1,2]
        """
        
        nums.sort()  ## O(nlogn)
        value=float('inf')
        for idx in range(len(nums)):
            integer_1=nums[idx]
            
            integers= nums[:idx]+nums[idx+1:]
            ## now binary search
            
            left=idx+1
            right=len(integers)-1
            
            while left<right:
                
                result=sum([integer_1,integers[left],integers[right]])
                
                ans=abs(result-target)
                if ans<value:
                    value=ans
                    closest_sum=result
                if target-result==0:
                    
                    return result
                elif result > target:
                    right-=1
                else:
                    left+=1
        return closest_sum
                
