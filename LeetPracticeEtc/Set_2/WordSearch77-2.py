board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word =  "ABCCED" #"A"  #"ABCCED"

def exist(board, word):

    w=len(word)
    m=len(board)
    n=len(board[0])

    def backtrack(i,j,l):
        
        if word[l]!=board[i][j]:
            return False

        if w==l+1:
            # print("True")
            return True
        
        temp=board[i][j]
        board[i][j]="#"        
        for off in [[0,1],[0,-1],[-1,0],[1,0]]:
            r=i+off[0]
            c=j+off[1]
            if 0<=r<m and 0<=c<n:
                # print("r,c,l:",r,c,l)
                if backtrack(r,c,l+1):
                    return True
        board[i][j]=temp
        return False

    for i in range(m):
        for j in range(n):
            backtrack(i,j,0)
            if backtrack(i,j,0):
                return True
    return False

exist(board,word)