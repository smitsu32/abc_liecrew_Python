from collections import defaultdict

n,k=map(int, input().split())
a=list(map(int, input().split()))

d=defaultdict(int)
for i in range(n):
    d[a[i]]+=1

l=[]
for key,v in d.items():
    l.append(key*v)
l.sort()

ans=sum(l[:max(0,len(l)-k)])
print(ans)