class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        runtime O(N), space O(1)
        """
        carry=1

        for idx in range(len(digits)-1,-1,-1):

            if carry+digits[idx]<=9:
                digits[idx]=carry+digits[idx]
                carry=0
            else:
                digits[idx]=0
                carry=1

        return digits if carry==0 else [carry]+digits
