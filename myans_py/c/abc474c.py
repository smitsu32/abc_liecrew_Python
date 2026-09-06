n,q=map(int, input().split())
p=list(map(int, input().split()))
ind=[0]*n
for i in range(n):
    ind[p[i]-1]=i

for i in range(q):
    a=int(input())
    p[ind[a-1]]=0
    p.append(a)
    ind[a-1]=n+i

ans=[]
for i in p:
    if i!=0:
        ans.append(i)
print(*ans)