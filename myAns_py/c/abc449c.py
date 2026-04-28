n,l,r=map(int, input().split())
s=input()

ans,cnt=0,[0]*26
for i in range(n):
    if i-l>=0:
        cnt[ord(s[i-l])-ord('a')]+=1
    if i-r-1>=0:
        cnt[ord(s[i-r-1])-ord('a')]-=1 # [l,r)
    ans+=cnt[ord(s[i])-ord('a')]

print(ans)