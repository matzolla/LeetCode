class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        result=[]
        
        for val in digits[::-1]:
            
            if (carry+val)<10:
                result.append(carry+val)
                carry=0
            else:
                result.append(0)
                carry=1
            
        return result[::-1] if carry==0 else [carry]+result[::-1]



# space complexity O(n) with n=len(array)

# time complexity O(n)  with n=len(result)
