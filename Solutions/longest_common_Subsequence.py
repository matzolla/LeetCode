class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        'ace'
        'abcde'
        
        """dp=[ [0,1,1,1,1]
                [1,1,2,0,0]
                [0,0,0,0,0] ]"""
        m,n=len(text1),len(text2)
        for i in range(1,len(text1)):
            for j in range(1,len(text2))
        if text1[i-1]==text2[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        ## time complexity is O(n^2)
        ## space O(dp) :)
        
        return dp[m-1][n-1]
