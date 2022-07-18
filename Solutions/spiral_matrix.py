"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral=[]
        columns=len(matrix[0])
        rows=len(matrix)
        row=0
        col=0
        flatten=[]
        if rows==1:
            return matrix[0]
        if columns==1:
            for list_ in matrix:
                flatten+=list_
            return flatten
        while row<rows-1 and col<columns-1:
            ## left
            for ids in range(col,columns-col-1):
                spiral.append(matrix[row][ids])
            ## down    
            for ids in range(row,rows-row):
                spiral.append(matrix[ids][columns-col-1])
            ## right
            
            for ids in range(columns-col-2,col,-1):
                spiral.append(matrix[rows-1-row][ids])
            ## top
            for ids in range(rows-row-1,row,-1):
                spiral.append(matrix[ids][col])
            
            row+=1
            col+=1
        return spiral if len(spiral)==rows*columns else spiral[:rows*columns]
    ## the time complexity is of the other of O(N^2)
    ## the space complexity is of the other of O(column*rows)