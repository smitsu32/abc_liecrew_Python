s=input()
t=input()
n,m=len(s),len(t)

# そのindex以降にある次文字のindexを格納
# n:abbab, ind[a]=[1,3,3,3,inf]
ind=[[10**6]*(n+1) for i in range(26)]
for i in range(n-1,-1,-1):
    for j in range(26):
        if chr(ord('a')+j)==s[i]:
            ind[j][i]=i
        else:
            ind[j][i]=ind[j][i+1]

ans=0
# 左端を変えてl~r未満の数を返す
for l in range(n):
    r=l
    for c in t:
        if r>=n:
            r=n+1
            break
        r=ind[ord(c)-ord('a')][r]
        if r>=n:
            r=n+1
            break
        r+=1
    ans+=r-l-1
print(ans)