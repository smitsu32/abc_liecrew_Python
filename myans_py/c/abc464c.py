n,m=map(int, input().split())
adb=[list(map(int, input().split())) for i in range(n)]
adb.sort(key=lambda x:x[1])

ans,j=0,0
cnt=[0]*(n+1)
for i in range(n):
    cnt[adb[i][0]]+=1
    if cnt[adb[i][0]]==1:
        ans+=1

for i in range(m):
    while j<n and adb[j][1]==i+1:
        cnt[adb[j][0]]-=1
        if cnt[adb[j][0]]==0: ans-=1
        cnt[adb[j][2]]+=1
        if cnt[adb[j][2]]==1: ans+=1
        j+=1
    print(ans)