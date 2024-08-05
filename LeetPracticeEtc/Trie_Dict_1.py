class Trie:
    def __init__(self) -> None:
        self.trie = {}
    
    def insert(self, word: str):
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        
        d["."] = "."

    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]
            # print(d[c])
        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for c in prefix:
            d = self.trie

            for c in prefix:
                if c not in d:
                    return False
                d = d[c]
            return True

trie = Trie()

trie.insert("apple")
a = trie.search("apple")   # returns true
# b = trie.search("app")     #// returns false
# c = trie.startsWith("app") #// returns true
# trie.insert("app")
# d = trie.search("app")     #// returns true

# print(a, b, c, d)

print(a)