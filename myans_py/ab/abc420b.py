n,m=map(int, input().split())
s=[input() for i in range(n)]

ans=[0]*n
for i in range(m):
    cnt=[0,0]
    for j in range(n):
        cnt[int(s[j][i])]+=1
    
    f=0
    if n//2>=cnt[1]:
        f=1
    
    for j in range(n):
        if int(s[j][i])==f:
            ans[j]+=1

cur=[]
for i in range(n):
    if ans[i]==max(ans):
        cur.append(i+1)
print(*cur)