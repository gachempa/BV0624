board = [["5","3",".",".","7",".",".",".","."],["6",".","1","2",".","5",".","8","9"]]

i, j = 0, 0
nums=["1","2","3","4","5","6","7","8","9"]

def mtree(i,j,board):
    if j==9:
        i+=1
        j=0

    print("i,j,board",i,j,board)

    if i==2:
        return board
    
    if i<1 and j>0:
        if board[i][j-1]==board[i+1][j-1]:
            return False
    
    if board[i][j]==".":
        for num in nums:
            if num not in board[i]:
                board[i][j]=num
                # print("i, j, num, board: ", i,j,num, board)
                if mtree(i,j+1,board):
                    return True
    else: 
        mtree(i,j+1,board)


mtree(0,0,board)
print(board)