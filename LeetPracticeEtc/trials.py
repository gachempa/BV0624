#  works but need to spped ip ... another version for that

nums = [-2,0,0,2,2]

ans_list=[]
add_flag=0
nums_freq={}
for n in nums:
    if n in nums_freq:
        nums_freq[n]+=1
    else:
        nums_freq[n]=1
# print(nums_freq)

if 0 in nums_freq and nums_freq[0]>=3:
    ans_list.append([0,0,0])

for i in range(len(nums)-2):
    x=nums[i]
    sum=0-x
    # print("sum",sum)
    for j in range(i+1,len(nums)-1):
        jsum=sum-nums[j]
        if jsum in nums_freq:
                     
            if (jsum==nums[j] and jsum==nums[i]):
                if nums_freq[jsum]>2: add_flag=1

            elif (jsum==nums[j] or jsum==nums[i]):
                  if nums_freq[jsum]>1: add_flag=1

            elif (jsum!=nums[j] and jsum!=nums[i]):
                add_flag=1
            
            if add_flag==1:
                a=sorted([nums[i],nums[j],jsum])
                if a not in ans_list: ans_list.append(a)
                add_flag=0

            print("i, j, jsum:",i,j,nums[i],nums[j], jsum)
            print("a",a)
            
            # or \
            #     ((jsum==nums[j] or jsum==nums[i]) and nums_freq[jsum]>1) or \
            #         (jsum!=nums[j] and jsum!=nums[i]):
            #     a=sorted([nums[i],nums[j],jsum])
            #     if a not in ans_list:
            #         ans_list.append(a)
            #         print("i, j, jsum:",i,j,nums[i],nums[j], jsum)
            #         print("a",a)

            # elif jsum!=nums[j] and jsum!=nums[i]:
            #     a=sorted([nums[i],nums[j],jsum])
            #     if a not in ans_list:
            #         ans_list.append(a)
                # print("a",a)
        # print("jsum",jsum)
    # print(sum)

print(ans_list)