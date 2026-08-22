n,m,k=map(int, input().split())
a=list(map(int, input().split()))

sm=0
f=[False]*n
for i in range(n):
    if i-m>=0 and f[i-m]:
        sm-=a[i-m]
    
    if sm+a[i]<=k:
        print('Yes')
        sm+=a[i]
        f[i]=True
    else:
        print('No')