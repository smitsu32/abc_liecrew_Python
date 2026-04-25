from collections import defaultdict

n=int(input())
s=input()

# ab[i]: a-b=iとなる要素数
ab,bc,ca,abc=defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)
ab[0]=bc[0]=ca[0]=abc[(0,0)]=1

a,b,c=0,0,0
ans=n*(n+1)//2
# 右端を動かし数える←連想配列
for i in s:
    if i=='A': a+=1
    elif i=='B': b+=1
    else: c+=1
    ans-=ab[a-b]+bc[b-c]+ca[c-a]
    ans+=2*abc[(a-b,b-c)] #3種包含
    
    ab[a-b]+=1
    bc[b-c]+=1
    ca[c-a]+=1
    abc[(a-b,b-c)]+=1

print(ans)