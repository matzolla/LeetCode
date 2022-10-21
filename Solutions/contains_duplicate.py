class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        
        
        Time complexity O(N), space complexity O(1)
        
        """
        
        hashtable={}
        
        hashset=set()
        
        for idx, num in enumerate(nums):
            
            if (num in hashset) and (abs(idx-hashtable[str(num)])<=k):
                return True
            else:
                hashtable[str(num)]=idx
                hashset.add(num)
        return False
