n,q=map(int, input().split())
a=list(map(int, input().split()))
s,now=[0],0
for i in range(n):
    now+=a[i]
    s.append(now)

ofs=0
for _ in range(q):
    qu=list(map(int, input().split()))
    if qu[0]==1:
        ofs=(ofs+qu[1])%n
    else:
        l,r=(qu[1]-1+ofs)%n,(qu[2]-1+ofs)%n
        if l<=r:
            print(s[r+1]-s[l])
        else:
            print(s[-1]-s[l] + s[r+1]-s[0])