# https://leetcode.com/problems/shortest-palindrome/description/

# s = "abcd"
# s = "aacecaaa"
# s = "aabba"
s = "aadcba"
a=len(s)

# while a>0:
#     s1 = s[:a]
#     if s1[:] == s1[::-1]:
#         s2 = s[a:]
#         print(s2[::-1]+s)
#         break
#     a -=1

while a>0:
    if s[:a][:] == s[:a][::-1]:
        print(s[a:][::-1]+s)
        break
    a -=1



print(a)