from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

n,q=map(int, input().split())

# 一番下のカード番号を管理
l=[i for i in range(n)]

for i in range(q):
    c,p=map(int, input().split())
    l[c-1]=p-1

ans=[0]*n
@lru_cache(maxsize=None)

def f(i):
    if l[i]==i:
        return i
    return f(l[i])

for i in range(n):
    j=f(i)
    ans[j]+=1

print(*ans)