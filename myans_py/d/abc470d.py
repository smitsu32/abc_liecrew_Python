n,q=map(int, input().split())
p=list(map(int, input().split()))

rev=False # 反転してるか
pr=[0]*n
for i in range(n):
    pr[p[i]-1]=i+1 # 中身は1-indexed(pが1~Nだから)

for _ in range(q):
    qu=list(map(int, input().split()))
    if qu[0]==1:
        x,y=qu[1]-1,qu[2]-1
        if not rev:
            pr[p[x]-1],pr[p[y]-1]=pr[p[y]-1],pr[p[x]-1] # p[x]書き換え前に
            p[x],p[y]=p[y],p[x]
        else:
            p[pr[x]-1],p[pr[y]-1]=p[pr[y]-1],p[pr[x]-1]
            pr[x],pr[y]=pr[y],pr[x]
    else:
        rev^=True

if not rev:
    print(*p)
else:
    print(*pr)