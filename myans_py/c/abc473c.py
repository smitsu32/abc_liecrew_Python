from collections import defaultdict

n,k=map(int, input().split())
a=list(map(int, input().split()))
d=defaultdict(int)
for i in range(n):
    d[a[i]]+=1
mx=max(d.values())

ans=0
for k,v in d.items():
    if v+1>=mx:
        ans+=1
print(ans)