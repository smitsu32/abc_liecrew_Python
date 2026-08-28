from bisect import bisect_right

n,q=map(int, input().split())
a=sorted(list(map(int, input().split())))
c=[0]
for i in range(n):
    c.append(c[-1]+a[i])

a.append(a[-1]+1)
for i in range(q):
    b=int(input())
    r=bisect_right(a,b)
    if r>=n+1:
        print(-1)
    else:
        r=bisect_right(a,b-1)
        print(c[r]+(b-1)*(n-r)+1) #b個未満となるようにすべて足して+1