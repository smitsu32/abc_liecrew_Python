n=int(input())
s=input()

ans=10**18
for si in ['A','B']:
    ansi,cnt=0,0
    for i in range(2*n):
        if s[i]==si:
            ansi+=abs(i-cnt*2)
            cnt+=1
    ans=min(ans,ansi)

print(ans)