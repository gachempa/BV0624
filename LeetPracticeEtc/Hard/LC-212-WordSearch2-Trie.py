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

