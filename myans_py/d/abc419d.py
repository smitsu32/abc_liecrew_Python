n,m=map(int, input().split())
s,t=input(),input()

cnt=[0]*(n+1)
for i in range(m):
    l,r=map(int, input().split())
    cnt[l-1]+=1
    cnt[r]-=1

ans,now=[],0
for i in range(n):
    now+=cnt[i]
    if now%2==0:
        ans.append(s[i])
    else:
        ans.append(t[i])

print(*ans,sep='')