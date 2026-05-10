n,a,b=map(int, input().split())
s=input()

sa,sb=[0],[0]
ca,cb=0,0
for i in range(n):
    if s[i]=='a':
        ca+=1
    else:
        cb+=1
    sa.append(ca)
    sb.append(cb)

ans=0
ra,rb=0,0
for l in range(n):
    # a以上
    while ra<=n and sa[ra]-sa[l]<a:
        ra+=1
    
    # b未満（+1をみる）
    rb=max(rb,l)
    while rb+1<=n and sb[rb+1]-sb[l]<b:
        rb+=1
    
    ans+=max(0,rb-ra+1)

print(ans)