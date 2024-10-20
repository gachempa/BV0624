# https://leetcode.com/problems/contains-duplicate-iii/description/

# nums = [1,2,3,1] 
# indexDiff = 3
# valueDiff = 0

nums = [1,5,9,13,17,1,5,9,8]
indexDiff = 2
valueDiff = 3

dict_D = {}
for i,num in enumerate(nums):
    k = num//(valueDiff+1)
    print(num,k)
    if k in dict_D and abs(dict_D[k][0]-i)<=indexDiff:
        print("True")
        break
    if k+1 in dict_D and abs(dict_D[k+1][0]-i)<=indexDiff and abs(dict_D[k+1][1]-num)<=valueDiff:
        print("True")
        break
    if k-1 in dict_D and abs(dict_D[k-1][0]-i)<=indexDiff and abs(dict_D[k-1][1]-num)<=valueDiff:
        print("True")
        break
    dict_D[k]=[i,num]
    # if(len(dict_D)>indexDiff):
    #     del dict_D[i-indexDiff]
print("False")
print(dict_D)