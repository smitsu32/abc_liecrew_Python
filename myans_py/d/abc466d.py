n,m=map(int, input().split())
rc=[list(map(int, input().split())) for i in range(m)]

# 逆順に探索（i番目以降で削除されない→降順で登場していない）
ans=0
r,c=set(),set()
for ri,ci in reversed(rc):
    if ri not in r and ci not in c:
        ans+=1
    r.add(ri)
    c.add(ci)

print(ans)