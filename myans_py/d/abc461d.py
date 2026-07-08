from collections import defaultdict

h,w,k=map(int, input().split())
s=[list(map(int, input())) for i in range(h)]
cnt=[[0]*(w+1) for i in range(h+1)]

for i in range(h):
    for j in range(w):
        cnt[i+1][j+1]=s[i][j]+cnt[i+1][j]+cnt[i][j+1]-cnt[i][j]

# 累積和を保存する配列は最初に定義、使った箇所だけ初期化(TLE防止)
sm=[0]*(h*w+1) #各行範囲ごとの要素iの個数

ans=0
for i1 in range(1,h+1):
    for i2 in range(i1,h+1):
        used=[]
        sm[0]=1
        used.append(0)
        cur=0 #今の合計
        for j in range(1,w+1):
            cur=cnt[i2][j]-cnt[i1-1][j]
            ans+=sm[cur-k] #s-kの個数にkを足したらOK
            sm[cur]+=1
            used.append(cur)

        for j in used:
            sm[j]=0

print(ans)