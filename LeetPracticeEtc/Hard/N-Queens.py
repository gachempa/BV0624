n = 4

idx=["0","1","2","3","4","5","6","7","8"]
choices, blocked = [], set()
ans, sol = [], []
Qs = n
count=0

for i in range(n):
    for j in range(n):
        choices.append(idx[i]+idx[j])
# print(choices)

def soln(Qs,blocked):
    global count

    # print("Qs count blocked" ,Qs, count, blocked)
    if Qs==0:
        sol.sort()
        if sol not in ans:
            ans.append(sol[:])
        return

    for ch in choices:
        if Qs+int(ch[0])>n:
            return ans
        if ch not in blocked and ch not in sol: 
            count+=1
            sol.append(ch)
            # print("ch sol:",ch, sol)
            ch_blocks=set(q_block(int(ch[0]),int(ch[1])))
            soln(Qs-1,blocked | ch_blocks)     
            sol.pop()
        

def q_block(r=0,c=0):
    gq_bloc=set()
    gq_bloc= horz(r,c) | vert(r,c) | diag(r,c)
    return gq_bloc

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


soln(Qs,blocked)
print(ans)
s_ans=[]

for i in range(len(ans)):
    l=[]
    s=""
    s_ans.append(l)
    for j in range(n):
        for _ in range(n):
            if _ == int((ans[i][j])[1]):
                s=s+"Q"
            else:
                s=s+"."
        l.append(s)
        s=""
        # print(l)
print(s_ans)

# testr, testc = 0, 0
# print(horz(testr,testc))
# print(vert(testr,testc))
# print(diag(testr,testc))
# print(q_block(testr,testc))