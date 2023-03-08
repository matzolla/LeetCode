class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        two pointers makes more sense

        a b c a
          _ 
          _
        """
        "abca"

        left=0
        right=len(s)-1
        delete_count_left=0
        delete_count_right=0
        while left <= right:

            if s[left]!=s[right]:
                right-=1
                delete_count_right+=1
            else:
                left+=1
                right-=1
        left=0
        right=len(s)-1
        while left <= right:
            if s[left]!=s[right]:
                left+=1
                delete_count_left+=1
            else:
                left+=1
                right-=1
        
        return (delete_count_left <=1) or (delete_count_right<=1)
