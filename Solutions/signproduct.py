class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        # time complexity O(n)
        # space complexity O(1)
        """

        product=1

        for val in nums:
            product*=val

        
        if product>0:return 1
        elif product<0: return -1
        else: return 0
