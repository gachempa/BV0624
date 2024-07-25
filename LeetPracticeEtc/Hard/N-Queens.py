n = 4

idx=["0","1","2","3","4","5","6","7","8"]
choices=[]
blocked=[]
ans=[]

for i in range(n):
    for j in range(n):
        choices.append(idx[i]+idx[j])

print(choices)




def soln(choices=choices,blocked=blocked,q=0,Qs=[]):
    if q==n:
        return ans
    if len(blocked)==len(choices):
        return False
    for ch in choices:
        if ch in blocked and ch==choices[-1]: return False
        if ch not in blocked:
            Qs.append(ch)
            blocked = blocked | horz(ch[0],ch[1]) | vert(ch[0],ch[1]) | diag(ch[0],ch[1])
            if soln(choices):return True        
            else: board[i][j]="."

def horz(r=0,c=0):
    ghorz=set()
    for c in range(n):
        ghorz.add(str(r)+str(c))
    return ghorz

def vert(r=0,c=0):
    gvert=set()
    for r in range(n):
        gvert.add(str(r)+str(c))
    return gvert

def diag(r=0,c=0):
    gdiag=set()
    r1=r
    c1=c
    while r<n and c<n:
        gdiag.add(str(r)+str(c))
        r+=1
        c+=1
    r,c=r1,c1
    while r>=0 and c<n:
        gdiag.add(str(r)+str(c))
        r-=1
        c+=1 
    r,c=r1,c1  
    while r<n and c>=0:
        gdiag.add(str(r)+str(c))
        r+=1
        c-=1
    r,c=r1,c1
    while r>=0 and c>=0:
        gdiag.add(str(r)+str(c))
        r-=1
        c-=1
    r,c=r1,c1
    return gdiag

print(horz(2,1))
print(vert(2,1))
print(diag(2,1))