class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        
        time complexity still of O(n^2) despite the dp aspect :), need to be optimize
        """
        array=[]
        
        for start,end,prof in zip(startTime,endTime,profit):
            
            array.append((start,end,prof))
            
        # now let's sort the array
        def overlapp(arr1,arr2):
            ## comparing two arrays and 
            ## return a boolean if the overlapp or not
            
            if (arr2[0]<arr1[1]) or (arr1[1]>arr2[1]) or ((arr1[0]==arr2[0])and(arr1[1]!=arr2[1])): return True
            else: return False
            
        array.sort()
        print(array)
        
        dp=[0]*len(array)
        dp[0]=array[0][2]
        
        for idx in range(1,len(array)):
            
            for idy in range(0,idx):
                if overlapp(array[idy],array[idx]):
                    dp[idx]=max(dp[idx],array[idx][2])
                else:
                    dp[idx]=max(dp[idx],dp[idy]+array[idx][2])
  
        return max(dp)
        
