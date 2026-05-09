n,k=map(int, input().split())
l,a=[],[]
for i in range(n):
    la=list(map(int, input().split()))
    l.append(la[0])
    a.append(la[1:])
c=list(map(int, input().split()))

for i in range(n):
    if k-c[i]*len(a[i])>0:
        k-=c[i]*len(a[i])
    else:
        k=(k-1)%len(a[i])
        print(a[i][k])
        exit()