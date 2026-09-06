n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=[a[i]-b[i] for i in range(n)]
INF=10**18

ans,w=[],0
for i in range(n):
    if c[i]<0:
        ans.append(1)
        w+=c[i]
    else:
        ans.append(INF)
        w+=c[i]*INF

if w>0:
    print('Yes')
    print(*ans)
else:
    print('No')