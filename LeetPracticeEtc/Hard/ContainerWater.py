height = [1,8,6,2,5,4,8,3,7]
# height = [1,8,6]

n=len(height)

max_vol=0

l_ptr=0
r_ptr=n-1

for i in range(n-1):
    print(i)
    max_vol=max(max_vol,min(height[l_ptr],height[r_ptr])*(n-i-1))
    print(max_vol)
    if height[l_ptr]<height[r_ptr]:l_ptr+=1 
    else: r_ptr-=1

print(max_vol)