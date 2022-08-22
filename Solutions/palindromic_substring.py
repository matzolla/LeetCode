class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        "a","aa","aaa","a","aa","a"
        result=[]
        for i in range(len(s)):
            
            for j in range(i,len(s)+1):
                if s[i:j]=="": continue
                if s[i:j]==s[i:j][::-1]: result.append(s[i:j])
                
        return len(result)
    
    
    ### time complexity O(n^3), the reason why i say so is because reversing a string has an O(n)
    ## time complexity, can be optimized to O(n^2) using dp
    
    ## space complexity is O(len(result)) but can be optimized to O(1)
