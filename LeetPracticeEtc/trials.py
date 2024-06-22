import re

# txt = "The rain in Spain"
# x=re.search("rain",txt)
# print(x)

Substring ='string'
 
 
String1 ='''We are learning regex with geeksforgeeks 
         regex is very useful for string matching.
          It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks 
         regex is very useful for string matching.
          It is fast too.'''
 
# Use of re.search() Method
print(1,re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(2,re.match(Substring, String1, re.IGNORECASE))
 
# Use of re.search() Method
print(3,re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(4,re.match(Substring, String2, re.IGNORECASE))

s3="abcbd"
p="a[bcd]*b"
x=re.match(p,s3)
y=re.match(fr"^{p}$", s3)
print(5,x)
print(6,y)

p ="a***abc"
while "**" in p:
    p = re.sub('\*\*', '*', p)
print("p",p)
