from collections import defaultdict

n=int(input())
d=defaultdict(int)

for x in range(1,int(n**0.5)+1):
    y=x+1
    while True:
        if x**2+y**2>n:
            break
        d[x**2+y**2]+=1
        y+=1

ans=[]
for k,v in d.items():
    if v==1:
        ans.append(k)

ans.sort()
print(len(ans))
print(*ans)