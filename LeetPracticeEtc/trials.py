#  test

valueDiff=3
visited = {0: 1, 3:10}
def dicReturn(x,y):
    if y-1 in visited and visited[y-1]-x <= valueDiff:
        return True
    if y+1 in visited and visited[y+1]-x <= valueDiff:
        return True
print(dicReturn(8,2))

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"

# pos=[0,0]
# for off in [[0,1],[0,-1],[-1,0],[1,0]]:
#     r=pos[0]+off[0]
#     c=pos[1]+off[1]
#     if r>=0 and c>=0:
#         pass

# n=4
# l = [[1, 3, 0, 2], [2, 0, 3, 1]]
# s = [["."*(x)+"Q"+"."*(n-x-1) for x in y] for y in l]
# print(s)

# lst = [[[x for x in range(5)] for x in range(5)] for x in range(5)]
# print(lst)

# nums=["1","2","3","4","5","6","7","8","9"]
# exclude= {'3', '5', '6', '8', '4', '1', '7', '9', '2', '.'}
# set_nums=set(nums)
# if set_nums.issubset(exclude):
#     print("yes")

# n=3
# k=3
# for i in range(k,k+3):
#     print(i)

# q1=int(n/k)
# q,r=divmod(n,k)
# print(q1)