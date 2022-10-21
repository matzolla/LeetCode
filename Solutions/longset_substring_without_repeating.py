class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        a b c a b c b b
        1 2 3
       Dynamic programming
       dp={}
       
       last_seen=s[0]
       dp[last_seen]=1
       
       for idx in range(1,len(s)):
         if s[idx] in hashset:
            curr_max=1
            ## we should add last_seen here also
         elif last_seen!=s[idx]:
           curr_max +=dp[last_seen]
         else:
            dp[s[idx]]=1
         
         last_seen=s[idx]
         hashset.add(s[idx])
         
         if curr_max> logest_substring:
         
            longest_substring=curr_max
            
        Time complexity O(N), space complexity O(len(dp))
        """
        
