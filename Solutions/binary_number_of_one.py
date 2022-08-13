class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        return str(bin(n)).count('1')


## time complexity of the bin operation is O(Logn)
## space complexity O(1)