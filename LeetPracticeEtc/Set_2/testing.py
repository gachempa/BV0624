digits="24"

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
oput_len=1
k_len=len(digits)
k_s=[]

print(key_map["2"][0])
print(len(key_map["9"]))
for i in range(k_len):
    k_alph=len(key_map[digits[i]])
    k_s.append(f"k{i}")
    k_s[i]=k_alph
    oput_len=oput_len*k_alph

    print("no.,", "alphs:", k_alph, key_map[digits[i]])

for i in range(k_s[0]):
    if k_len<2:
        oput.append("g")
    elif k_len<3:
        for j in range(k_s[1]):
        #    x=key_map[digits[i]]
           oput.append("h")

print(k_s[0])
print(oput_len)
print(oput)

# for i in range(oput_len):
#     # for j in range(k_len)

#     oput.append("-"*k_len)

# print(oput[0:6])
# oput[0]="abc"
# print(oput[0:6])
# # key_map["2"][0]