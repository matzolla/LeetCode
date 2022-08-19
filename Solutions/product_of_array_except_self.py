class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ##let's checkout the prefix product and suffix product
        
        ##nums: 1   2    3     4
        ## pre: 1   1    2     6
        ##suff: 24  12   4     1
        
        ##res:  24  12   8     6
        
        result=[]
        ## prefix
        preffix=[]
        
        curr=1
        
        for i in range(len(nums)):
            
            preffix.append(curr)
            curr*=nums[i]
        ## suffix
        suffix=[]
        
        curr=1
        
        for i in range(len(nums)-1,-1,-1):
            
            suffix.append(curr)
            curr*=nums[i]
        
        reverse_suffix=suffix[::-1]
        
        for i in range(len(nums)):
            result.append(preffix[i]*reverse_suffix[i])
        
        return result
      
      ## time O(n)
      ## space O(3n)
