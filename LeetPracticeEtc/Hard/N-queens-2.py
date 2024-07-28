n=4

def DFS(queens, xy_dif, xy_sum):
    p = len(queens)
    if p==n:
        result.append(queens)
        return None
    for q in range(n):
        # print(p,q, queens, xy_dif, xy_sum)
        if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
            DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
result = []
DFS([],[],[])
print(result)
# print([ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result])