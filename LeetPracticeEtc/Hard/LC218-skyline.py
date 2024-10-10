# https://leetcode.com/problems/the-skyline-problem/description/

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
ans=[]
prev_ht = 0

starts_min=min([innerlist[0] for innerlist in buildings])
ends_max=max([innerlist[1] for innerlist in buildings])
buildings.append((starts_min,ends_max+1,0)) #needed to take care of 0 height
print(starts_min,ends_max)

for i in range(starts_min,ends_max+1):
    y_ht = max([innerlist[2] for innerlist in buildings 
                if innerlist[0] <= i  
                if innerlist[1] > i ]) 
    if y_ht == prev_ht:
        pass
    else:
        ans.append((i, y_ht))
        prev_ht = y_ht
    print(i, y_ht)

print(ans)