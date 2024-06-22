num=3749

dict_1={
    1:"I",
    4:"IV",
    5:"V",
    9:"IX",
    10:"X",
    40:"XL",
    50:"L",
    90:"XC",
    100:"C",
    400:"CD",
    500:"D",
    900:"CM",
    1000:"M",
}

list_1=[]
count=0
flag=0
while num>0:
    x=(num%10*10**count)
    if x in dict_1:
        list_1.insert(0,dict_1[x])
    elif x/10**count>5:
        t=dict_1[5*10**count]
        i=x-5*10**count
        while i>0:
            list_1.insert(0,dict_1[10**count])
            i-=10**count
        list_1.insert(0,t)
    else:
        i=x
        while i>0:
            list_1.insert(0,dict_1[10**count])
            i-=10**count
    # print(list_1)
    # print(x)
    num=int(num/10)
    # print(num)
    count+=1

print(list_1)
final=''.join(list_1)
print(final)