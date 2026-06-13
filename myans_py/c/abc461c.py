n,k,m=map(int, input().split())
cv=[list(map(int, input().split())) for _ in range(n)]
cv.sort(key=lambda x:-x[1])

used=set()
cnt=0
ans=0
other=[]
for i in range(n):
    if cv[i][0] not in used and cnt<m:
        used.add(cv[i][0])
        cnt+=1
        ans+=cv[i][1]
    else:
        other.append(cv[i])

other.sort(key=lambda x:-x[1])
for i in range(k-m):
    ans+=other[i][1]

print(ans)