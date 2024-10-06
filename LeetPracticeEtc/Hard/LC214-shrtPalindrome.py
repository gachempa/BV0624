# https://leetcode.com/problems/shortest-palindrome/description/

# s = "aabcd"
# s = "aacecaaa"
# s = "aabba"
s = "adcba"

l = len(s)
str1 = ""
a,b = 0,-1
while l-a+b>0:
    str1+=s[b]
    if s[a]==s[b]:
        a+=1 
        b-=1
        print("a=b",a,b)
        if l-a+b<0: b+=1
    else:
        b-=1
        print("a not= b",a,b)
        if l-a+b<=0: b-=1

print(s)
print(str1)
print(a,b,l)
ans = str1+s[b:]
print(ans)