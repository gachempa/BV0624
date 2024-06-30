nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2

nums.sort()
ans_sum=nums[0]+nums[1]+nums[2]
dx=ans_sum-target

for i in range(len(nums)):
    # print(i)

    if i>0 and nums[i]==nums[i-1]:
        continue

    j=i+1
    k=len(nums)-1

    while j<k and dx!=0:
        w_dx=(nums[i]+nums[j]+nums[k])-target
        # print("wdx",w_dx)
        if w_dx<0:
            j+=1
            # print("j",j)
            # while nums[j]==nums[j-1] and j<k:
            #     j+=1       
        elif w_dx>0:
            k-=1
            # while nums[k]==nums[k+1] and j<k:
            #     k-=1
        if abs(w_dx)<abs(dx):
            dx=w_dx

    if dx==0:
        # print("break")
        break

ans_sum=dx+target
print(ans_sum)