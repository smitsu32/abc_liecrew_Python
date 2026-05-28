from bisect import bisect_left,bisect_right

n,q=map(int, input().split())

ver=[1]*(n+1)
ver[0]=0
mn=1
for i in range(q):
    x,y=map(int, input().split())
    res=0
    while mn<=x:
        res+=ver[mn]
        ver[y]+=ver[mn]
        mn+=1
    print(res)