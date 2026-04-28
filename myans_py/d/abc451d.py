from collections import deque

d=deque()
p=[]
s=set()
for i in range(31):
    d.append(2**i)
    s.add(2**i)
    p.append(2**i)

while d:
    i=d.popleft()
    if len(str(i))>9:
        continue
    
    for j in range(31):
        ns=str(i)+str(p[j])
        if len(ns)>9:
            break
        
        ns=int(ns)
        if ns not in s:
            d.append(ns)
            s.add(ns)

ans=sorted([int(i) for i in s])

n=int(input())
print(ans[n-1])