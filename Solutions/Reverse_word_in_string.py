class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        
        # time complexity is O(N)
        # space complexity is O(N)
        """
        
        split_str=s.split()
        
        left=0
        right=len(split_str)-1
        
        while left<right:
            
            split_str[left],split_str[right]=split_str[right],split_str[left]
            
            left+=1
            right-=1
            
            
        return " ".join(split_str)
