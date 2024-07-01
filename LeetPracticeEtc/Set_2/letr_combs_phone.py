digits="29"

key_map = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

oput=[]
k_len=len(digits)


if k_len==4:
    x1=key_map[digits[0]]
    x2=key_map[digits[1]]
    x3=key_map[digits[2]]
    x4=key_map[digits[3]]
    for i in range(len(x1)):
        for j in range(len(x2)):
            for k in range(len(x3)):
                for l in range(len(x4)):
                    y1=key_map[digits[0]][i]
                    y2=key_map[digits[1]][j]
                    y3=key_map[digits[2]][k]
                    y4=key_map[digits[3]][l]
                    y=y1+y2+y3+y4
                    oput.append(y)

if k_len==3:
    x1=key_map[digits[0]]
    x2=key_map[digits[1]]
    x3=key_map[digits[2]]
    for i in range(len(x1)):
        for j in range(len(x2)):
            for k in range(len(x3)):
                y1=key_map[digits[0]][i]
                y2=key_map[digits[1]][j]
                y3=key_map[digits[2]][k]
                y=y1+y2+y3
                oput.append(y)

if k_len==2:
    x1=key_map[digits[0]]
    x2=key_map[digits[1]]
    for i in range(len(x1)):
        for j in range(len(x2)):
                y1=key_map[digits[0]][i]
                y2=key_map[digits[1]][j]
                y=y1+y2
                oput.append(y)

if k_len==1:
    x1=key_map[digits[0]]
    for i in range(len(x1)):
                y1=key_map[digits[0]][i]
                y=y1
                oput.append(y)

print(oput)
