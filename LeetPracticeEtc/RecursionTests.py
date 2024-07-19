def gridPaths(n,m):
    if n==1 or m==1:
        return 1
    else:
        gridPaths(n,m-1)+gridPaths(n-1,m)

p= gridPaths(3,3)
print(p)