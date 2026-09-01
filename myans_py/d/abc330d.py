n=int(input())
s=[input() for i in range(n)]

fh,fw=[0]*n,[0]*n
for i in range(n):
    for j in range(n):
        if s[i][j]=='o':
            fh[i]+=1
            fw[j]+=1

ans=0
for i in range(n):
    for j in range(n):
        if s[i][j]=='o' and fh[i]>=2 and fw[j]>=2: #そのマスは含みそれ以外から1マスずつ選ぶ
            ans+=(fh[i]-1)*(fw[j]-1)
print(ans)