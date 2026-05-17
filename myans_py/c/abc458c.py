s=input()
n=len(s)

ans=s.count('C')
for i in range(1,n-1):
    if s[i]=='C':
        ans+=min(i,n-i-1)

print(ans)