# storing english alphabets

class Trienode:
    def __init__(self) -> None:
        self.child = [None]*26
        self.wordEnd = False
    
def insert_key(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            new_node = Trienode()
            curr.child[index] = new_node
        curr=curr.child[index]
    curr.wordEnd = True

def searchKey(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False
        curr = curr.child[index]
    return curr.wordEnd

root = Trienode()
arr = ['and','ant','do','geek','dad','ball']
for s in arr:
    insert_key(root, s)

searchKey = ["do","gee","bat"]
for s in searchKey:
    print(f"Key : {s}")
    if searchKey(root, s):
        print("Present")
    else:
        print("not Present")