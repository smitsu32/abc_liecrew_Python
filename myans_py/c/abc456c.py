s=input()
MOD=998244353

ans=0
cur=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        cur+=1
    else:
        ans+=cur*(cur+1)//2
        cur=1
ans+=cur*(cur+1)//2

print(ans%MOD)