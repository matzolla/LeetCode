class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        idx
        """
        ## condition 1 if len(s)==0
        if len(s)==1: return s

        ## condition 2 if len(s)==2

        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]

        ### condition 3 if len(s)>=3

        dp=[[False for idx in range(len(s))] for idy in range(len(s))]

        curr_word=""

        curr_length=0
        for idx in range(len(s)):
            for idy in range(len(s)):

                dp[idx][idx]=True

        for idx in range(1,len(s)):

            for idy in range(0,idx):

                if s[idx]==s[idy] and (dp[idx-1][idy+1] or abs(idx-idy)==1):

                    dp[idx][idy]=True
                    if curr_length< idx+1-idy:
                        curr_length=idx+1-idy
                        curr_word=s[idy:idx+1]
        return curr_word
