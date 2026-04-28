h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]

sumh=[sum(row) for row in a]
sumw=[sum(col) for col in zip(*a)]

for i in range(h):
    for j in range(w):
        a[i][j]=sumh[i]+sumw[j]-a[i][j]

for li in a:
    print(*li)