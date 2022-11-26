class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        envelopes=[[2, 3], [5, 4], [6, 4], [6, 7]]
        dp=       [  1,      2,       2,      3]
        
        dp[i]=max(dp[i],dp[j]+1)
        
        time complexity O(N^2 + nlogn)
        space O(N)
        """
        #[1,2,3,4]
        envelopes.sort()
        dp=[1]*len(envelopes)
        
        for idx in range(1,len(envelopes)):
            
            for idy in range(0,idx):
                
                if (envelopes[idy][0]<envelopes[idx][0]) and (envelopes[idy][1]<envelopes[idx][1]):
                    
                    dp[idx]=max(dp[idx],dp[idy]+1)
                    
                    
        return max(dp)
