
"""
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. 
The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.
"""
class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        lookup={}
        
        alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ### generating a lookup table in the form lookup={'A':0,'B':1......}
        for i,ch in enumerate(alph):
            lookup[ch]=i
        
        ## initializing the final output
        char=""
        
        max_val=0
        
        ## create a set 
        set_s= set(s)
        stack=set()
        
        for alphabet in set_s:
            # if alphabet is upper  check if lower in s 
            if alphabet.isupper():
                if alphabet.lower() in set_s:
                    stack.add(alphabet)
            else:
                ## means alphabet lower check upper
                if alphabet.upper() in set_s:
                    
                    stack.add(alphabet.upper())

        for str_ in stack:
            
            if lookup[str_]>=max_val:
                max_val=lookup[str_]
                
                char=str_
                
                    
        return char

## I'm proud of this solution, leetcode contest number 298

## Time complexity O(N) space complexity O(M) M =len(stack)  could be extended to O(1)