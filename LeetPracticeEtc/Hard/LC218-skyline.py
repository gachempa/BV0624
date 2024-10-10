# https://leetcode.com/problems/the-skyline-problem/description/

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
ans=[]
prev_ht = 0

starts_min=min([innerlist[0] for innerlist in buildings])
ends_max=max([innerlist[1] for innerlist in buildings])
print(starts_min,ends_max)

for i in range(starts_min,ends_max):
    y_ht = max([innerlist[2] for innerlist in buildings 
                if innerlist[0] <= i for innerlist in buildings 
                if innerlist[1] > i for innerlist in buildings ]) 
    if y_ht == prev_ht:
        pass
    else:
        ans.append((i, y_ht))
        prev_ht = y_ht
    print(i)

print(ans)