s=input()
n=len(s)

ans=0
#奇数長:i文字から広げてく感じ
for i in range(n):
    l,r=i,i
    cnt=0
    while 0<=l and r<n:
        if s[l]!=s[r]:
            cnt+=1
            if cnt==2:
                break
        ans+=1
        l-=1
        r+=1

#偶数長:[i,i+1]文字から広げてく感じ
for i in range(n-1):
    l,r=i,i+1
    cnt=0
    while 0<=l and r<n:
        if s[l]!=s[r]:
            cnt+=1
            if cnt>=2:
                break
        ans+=1
        l-=1
        r+=1

print(ans)