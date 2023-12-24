"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least 
two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""

## example ####
## nums = [23,2,4,6,7], k = 6 [2,4] forms a contiguous sum cause 2+4=6 and 6%6=0

class solution(object):

    def contiguous_sum(self,array,k):
        # input: an array [list]
        # input: integer K
        # output: a contiguous sub array [list]

        ans=0
       
        for i in range(2,len(array)):

            for j in range(len(array)):

                ## compute sum:
                ans=sum(array[j:j+i])
                ## check conditions

                if ans%k==0: 
                    output=array[j:j+i]
                    return output ## or return True

        
        return False


### Time complexity O(m*n) (O(n^2) in the worst casw) and space complexity is O(1)

## pretty good attempt
            
