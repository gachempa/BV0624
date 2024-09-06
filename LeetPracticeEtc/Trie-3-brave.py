"""In Python, a Trie can be implemented using a 
dictionary to store the children of each node and 
a default value (e.g., an empty dictionary) to 
represent the root node. Each node in the Trie 
represents a character in a string, and the 
edges connect nodes with the same character.

Here’s a simplified code example:"""

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word_end = True
    
    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word_end

trie = Trie()
trie.insert("and")
trie.insert("ant")
trie.insert("dad")

print(trie.search("dad"))
print(trie.search("not"))
print(trie.search("da"))