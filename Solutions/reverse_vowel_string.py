class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        
        
        Time complexity is O(N)
        space complexity (may be auxillary? O(N)
        """
        
        letters=[char for char in s]
        
        hashset={'a','e','i','o','u'}
        
        left=0
        
        right=len(letters)-1
        
        while left<right:
            
            if (letters[left].lower() in hashset) and (letters[right].lower() in hashset):
                
                left_char=letters[left]
                right_char=letters[right]
                #### swap the letters
                
                letters[left]=right_char
                letters[right]=left_char
                
                left+=1
                right-=1
                
            elif (letters[left].lower() in hashset) and (letters[right].lower() not in hashset):
                right-=1
                
            elif (letters[left].lower() not in hashset) and (letters[right].lower() in hashset):
                left+=1
            else:
                left+=1
                right-=1
        
        
        return "".join(letters)
