# https://leetcode.com/problems/word-search-ii/description/

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

class Trienode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self) -> None:
        self.root = Trienode()

    def insert(self,word):
        currnode = self.root
        for char in word:
            if char not in currnode.children:
                currnode.children[char] = Trienode()
                print(char)
            currnode = currnode.children[char]
        currnode.is_word_end = True

def findWords(board, words):
    trie_ = Trie()
    for word in words:
        trie_.insert(word)
        print("hhh")
    rows, cols = len(board), len(board[0])
    visited = [[False]*cols for _ in range(rows)]
    ans = []

    def dfs(r, c, currnode, word):
        if r<0 or r>=rows or c<0 or c>=cols or visited[r][c] or board[r][c] not in currnode.children:
            return
        visited[r][c]=True
        currnode = currnode.children[board[r][c]]
        word += board[r][c]
        if currnode.is_word_end:
            ans.append(word)
            currnode.is_word_end = False # so the word will not be appended again to ans
        dfs(r+1,c,currnode,word)
        dfs(r-1,c,currnode,word)
        dfs(r,c+1,currnode,word)
        dfs(r,c-1,currnode,word)
        visited[r][c]=False

    for i in range(rows):
        for j in range(cols):
            dfs(i,j,trie_.root,"")
    print(ans)

findWords(board,words)