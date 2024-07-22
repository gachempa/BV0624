board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
i, j = 0, 0
nums=["1","2","3","4","5","6","7","8","9"]


def gfill(i=0,j=0,board=board):
    if j==9:
        i+=1
        j=0
    if i==9:
        return True

    elif board[i][j]==".":
        exclude = gseg(i,j,board) | gcol(j,board) | grow(i,board)
        if set(nums).issubset(exclude):
            return False 
        else:
            for num in nums:           
                if num not in exclude:
                    board[i][j]=num
                    if gfill(i,j+1,board):return True        
                    else: board[i][j]="."

    elif gfill(i,j+1,board):
            return True

def grow(i,board):
    grow1=set()
    for c in range(9):
        grow1.add(board[i][c])
    return grow1

def gcol(j,board):
    gcol1=set()
    for r in range(9):
        gcol1.add(board[r][j])
    return gcol1

def gseg(i,j,board):
    r=int(i/3)*3
    c=int(j/3)*3
    gseg1=set()
    for x in range(r,r+3):
        for y in range(c,c+3):
            gseg1.add(board[x][y])
    return gseg1

gfill()
print(board)

# lrow=grow(7,board)
# print(lrow)
# lcol=gcol(7,board)
# print(lcol)
# lseg=gseg(7,3,board)
# print(lseg)

# exclude=gseg(0,0,board) | gcol(0,board) | grow(0,board)
# print(exclude)

# if "4" not in exclude:
#     print("Not")