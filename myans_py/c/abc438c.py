n=int(input())
a=list(map(int, input().split()))

l=[]
for i in range(n):
    l.append(a[i])
    if len(l)>=4 and l[-1]==l[-2]==l[-3]==l[-4]:
        for i in range(4): del(l[-1])

print(len(l))