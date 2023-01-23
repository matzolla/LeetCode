class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        runtime is O(mn)
        space complexity O(m+n)
        """

        row_index= set()
        col_index= set()

        row= len(matrix)
        col= len(matrix[0])

        for r in range(row):

            for c in range(col):

                if matrix[r][c]==0:
                    row_index.add(r)
                    col_index.add(c)
        for Row in row_index:

            for c in range(col):

                matrix[Row][c]=0
        for r in range(row):

            for Col in col_index:

                matrix[r][Col]=0

        return matrix
