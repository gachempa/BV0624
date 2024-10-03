# https://leetcode.com/problems/shortest-palindrome/description/

s = "aacecaaa"

l = len(s)
str1 = ""

a,b = 0,-1
while l-a+b>0:
    str1+=s[b]
    if s[a]==s[b]:
        a+=1
        b-=1
    else:
        b-=1

result = str1+s
print(result)
print(str1)
print(a,b)
ans = str1+s[a:]
print(ans)