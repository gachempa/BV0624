str1 = "abc"
str2 = "bad"

set_str1=set(str1)
set_str2=set(str2)
# print(set_str1)

if len(set_str1) < len(set_str2):
    print(False)


j = i = 0
while i < len(str1) and j < len(str2):
    c1, c2 = str1[i], str2[j]
    if ord(c1) == ord(c2) or ord(c1) == ord(c2) - 1 or (c1 == "z" and c2 == "a"): 
        j += 1
    i += 1

print(j == len(str2))