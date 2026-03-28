from collections import deque
# 余りをとって最初+Kを後ろに回しつつ、差の最小値を探す
n,k=map(int, input().split())
a=list(map(int, input().split()))

b=[]
for i in range(n):
    b.append(a[i]%k)
b.sort()

b=deque(b)

ans=b[-1]-b[0]
for i in range(n):
    bi=b.popleft()
    b.append(bi+k)
    ans=min(ans,b[-1]-b[0])

print(ans)