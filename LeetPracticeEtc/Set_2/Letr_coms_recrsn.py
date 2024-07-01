digits="29"

if not digits:
    print([])

keymap = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }

k=[]
ans=[]

def dfs(i,k):

    if i==len(digits):
        ans.append("".join(k))
        return 
    for m in keymap[digits[i]]:
        k.append(m)
        print("pre-dfs k: ",k)
        dfs(i+1,k)
        print(k)
        k.pop()


dfs(0,k)
print(ans)