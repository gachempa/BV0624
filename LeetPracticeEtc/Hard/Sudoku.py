board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

i, j = 0, 0
nums=["1","2","3","4","5","6","7","8","9"]

# print(board[i][j])

def gfill(i=0,j=0,board=board):

    if i<9:
        if board[i][j]==".":
            print("i","j",i,j)
            exclude = gseg(i,j,board) | gcol(j,board) | grow(i,board)
            print("col:",gcol(j,board))
            print("exclude:",exclude)
            if set(nums).issubset(exclude):
                print("False")
                return False
            else:
                for num in nums:
                    if num not in exclude:
                        board[i][j]=num
                        print("i j num:",i,j,num)
                        j+=1
                        if j==9:
                            i+=1
                            if i == 9: return True
                            j=0
                        gfill(i,j,board)                        
                print(i,j)
        else:
            print("else","i","j",i,j)
            j+=1
            if j==9:
                i+=1
                if i == 9: return True
                j=0
            gfill(i,j,board)         

    # else:
    #     return False

def grow(i,board):
    grow1=set()
    for c in range(9):
        # grow1.append(board[i][c])
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
# lrow=grow(0,board)
# print(lrow)

print(board)

# exclude=gseg(0,0,board) | gcol(0,board) | grow(0,board)
# print(exclude)

# if "4" not in exclude:
#     print("Not")