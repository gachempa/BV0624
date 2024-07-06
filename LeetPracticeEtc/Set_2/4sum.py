nums = [2,2,2,2,2]
target = 8

nums.sort()
ans=[]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):

        t=nums[i]+nums[j]-target
        l=j+1
        r=len(nums)-1

        while r>l:
            t2=t+nums[l]+nums[r]
            # print("l","r",l,r)

            if t2>0:
                r-=1
            elif t2<0:
                l+=1
            else:
                if ([nums[i],nums[j],nums[l],nums[r]]) not in ans:
                    ans.append([nums[i],nums[j],nums[l],nums[r]])
                r-=1
                while nums[r]==nums[r+1] and r>l:
                    r-=1
                    # print("r",r)

print(ans)