n,q=map(int, input().split())
a=list(map(int, input().split()))
l=[]
for i in range(n):
    l.append([a[i],i+1])
l.sort()

for _ in range(q):
    k=int(input())
    b=set(map(int, input().split()))
    for i in range(n):
        if l[i][1] not in b:
            print(l[i][0])
            break