# https://leetcode.com/problems/basic-calculator/description/
import re

s = "(1+(4+5+2) -  3)+(6+8)"

s = f'({s.replace(" ","")})'

x = lambda y:str(sum(map(int,re.findall(r'[+-]?\d+',y[0]))))

while '(' in s:
    s = re.sub(r'\([^()]+\)',x,s).replace("--","+")

print(int(s))