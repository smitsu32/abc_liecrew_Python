n,d=map(int, input().split())
#imos
t=[0]*(10**6+1) #時間
for i in range(n):
    si,ti=map(int, input().split())
    if si<=ti-d: #犯行時間より長い時
        t[si]+=1
        t[ti-d+1]-=1

cur,ans=0,0
for i in range(10**6+1):
    cur+=t[i]
    if cur>=2:
        ans+=cur*(cur-1)//2

print(ans)