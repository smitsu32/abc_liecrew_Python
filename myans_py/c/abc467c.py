n,_=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

c=[0]*n
ans=10**18
for c0 in [0,1]:
    c[0]=c0
    for i in range(n-1):
        if b[i]!=(c[i]+c[i+1])%2:
            c[i+1]^=1

    ansi=0
    for i in range(n):
        ansi+=a[i]^c[i]
    ans=min(ans,ansi)

print(ans)