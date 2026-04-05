n=int(input())
ab=[]
for i in range(n):
    ai,bi=map(int, input().split())
    ab.append((ai,bi))
m=int(input())
s=[input() for i in range(m)]

f=[set() for i in range(n)]
for i in range(n):
    for j in range(m):
        if len(s[j])==ab[i][0]:
            f[i].add(s[j][ab[i][1]-1])

for i in range(m):
    flag=True
    if len(s[i])!=n:
        print('No')
        continue
    
    for j in range(n):
        if s[i][j] not in f[j]:
            flag=False
            break
    if flag:
        print('Yes')
    else:
        print('No')