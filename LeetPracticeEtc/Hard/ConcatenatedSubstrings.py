# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

s = "aaaaaaaaaa"
words = ["a","a","a","a","a"]

set_s=set(s)
set_words=set(words)
print(set_s,set_words)

ls = len(s)
lw = len(words)
lw0 = len(words[0])
ans=[]

if len(set_s)==1 and set_s==set_words:
    for i in range(ls-lw+1):
        ans.append(i)

# print(ls, lw, lw0)
else:
    for i in range(ls-lw*lw0+1):
        j=0
        twords = words[:]
        temp = s[i:i+lw0]
        if temp not in twords:
            continue
        else:
            while j<lw*lw0 and temp in twords:
                print(temp)
                twords.remove(temp)
                if len(twords)==0:
                    ans.append(i)
                print(twords)
                j+=lw0
                temp = s[i+j:i+lw0+j]

print(ans)