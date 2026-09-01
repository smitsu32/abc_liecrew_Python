n=int(input())
s=input()
c=list(map(int, input().split()))

# 0101 ... 1010 がどこかで入れ替わる
# → 4パターン必要
def f(b):
    a=[0]*n
    if s[0]!=str(b):
        a[0]=c[0]
    
    for i in range(1,n):
        b^=1
        if s[i]!=str(b):
            a[i]=a[i-1]+c[i]
        else:
            a[i]=a[i-1]
    return a

l0,l1=f(0),f(1)
s,c=s[::-1],c[::-1]
r0,r1=f(0),f(1)

ans=10**18
for i in range(n-1):
    j=n-i-2  #i+1からn-1
    if i%2==j%2: #長さの偶奇おなじ→入れ替わらない
        ans=min(ans,l0[i]+r0[j])
        ans=min(ans,l1[i]+r1[j])
    else:
        ans=min(ans,l0[i]+r1[j])
        ans=min(ans,l1[i]+r0[j])
        
print(ans)