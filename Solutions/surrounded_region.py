"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

"""

##Example


"""
_________        _________
|x|x|x|x|        |x|x|x|x|
|x|O|O|x|        |x|x|x|x|
|x|x|O|x|------> |x|x|x|x|
|x|O|x|x|        |x|O|x|x|
"""

def dfs(board,i,j):
    #input board: matrix
    #i,j: position of element in board
    #Output: bool (is_boarder or not)
    if (board[i-1,j]=="X")and(board[i+1,j]=="X")and(board[i,j-1]=="X")and(board[i,j+1]=="X"):
        return True
    else:
        return False

def is_boarder(board,i,j):
    #input board: matrix
    #i,j: position of element in board
    #Output: bool (is_boarder or not)
    row= board.shape[0]
    col=board.shape[1]

    if (i<=0 or i>= row)and(j<=0 or j>=col)and(board[i,j]=="O"):

        return 1
    else:
        return 0

def solve(board):
    # Input board matrix
    # Output: Modified board Matrix in place
    #

    result_indices=[] # this list captures the indices of the "O"
    result_score=[]   # this one captures the indices of the associated score

    for i in range(1,board.shape[0]-1):

        for j in range(1, board.shape[1]-1):

            if board[i,j]=="X":
                result_indices.append("X") 
                result_score.append(-1)
            else:
                bool=dfs(board,i,j)

                if bool: 
                    board[i,j]="X"
                    #capture
                else:
                    ##check_boarder
                    boarder_left=is_boarder(board,i-1,j)
                    boarder_right=is_boarder(board,i+1,j)
                    boarder_top=is_boarder(board,i,j-1)
                    boarder_bottom=is_boarder(board,i,j+1)

                    result=boarder_left+boarder_bottom+ boarder_right+ boarder_top
                    result_indices.append([i,j]) 
                    result_score.append(result)
                    board[i,j]=result

     ##### At the end of this stage the lists are like this : ["X",[0,1],[1,2],"X","X","X",[2,1],[3,1]] 
     ##### and scores[-1,0,2,-1,-1,-1,0,1] 
     # Time complexity O(mxn)
    ans=[[]]
    for i in range(len(result_indices)):
        if result_indices[i]!="X":
            ans[len(ans)-1].append(result_indices[i])
        else:
             ans.append([])
    ### result [[],[[0,1],[1,2]],[],[][[2,1],[3,1]]]
     

    return ans 
