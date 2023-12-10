class Solution(object):
    def lengthOfLongestSubstring(self, s):
       
        """
       time complexity O(n)
       
       """
       left=0
       right=0
       seen=set()

       longest_substring= -float('inf')
       while left<len(s) and right<len(s):
          if s[right] not in seen:
             curr_val= (right-left)+1
             seen.add(s[right])
             right+=1
          else:
             
             seen.remove(s[left])
             left+=1

          if curr_val>longest_substring:
             longest_substring=curr_val
          
          

       return longest_substring if len(s)>0 else 0
