n,m=map(int, input().split())

ans=0
put=set()
for i in range(m):
    r,c=map(int, input().split())
    f=True
    for dr,dc in [[0,0],[1,0],[0,1],[1,1]]:
        nr,nc=r+dr,c+dc
        if (nr,nc) in put or nr>n or nc>n:
            f=False
            break
    if f:
        ans+=1
        for dr,dc in [[0,0],[1,0],[0,1],[1,1]]:
            put.add((r+dr,c+dc))

print(ans)