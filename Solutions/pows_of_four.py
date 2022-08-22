class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """        divisor=4
        if n==1:return True
        while abs(n)>= divisor:
            
            if (abs(n)/divisor)==1: return True
            divisor*=divisor
            
        return False"""



        lookup=set()
        for power in range(16):
            lookup.add(4**power)
        return n in lookup
      
      
      ### time complexity O(len(lookup)) constant time complexity. O(1)
      ### space complexity O(constant) also doesnt change irrespectif of the number n (both time and space) O(1)
