# https://leetcode.com/problems/word-search-ii/description/

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
            currnode = currnode.children[char]
        currnode.is_word_end = True

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

trie_ = Trie()
for word in words:
    trie_.insert(word)

