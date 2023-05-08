class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        
        time complexity O(n), space complexity O(1)
        """
        result=0
        n=len(mat)
        if n==1: return mat[0][0]
        mid=n//2
        for idx in range(n):

            result+= mat[idx][idx]+ mat[idx][n-1-idx]

        return result-mat[mid][mid] if n%2!=0 else result
