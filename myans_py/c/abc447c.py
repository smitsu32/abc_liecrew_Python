s=input()
t=input()
sa,ta=[],[]
swo,two=[],[]

now=0
for i in range(len(s)):
    if s[i]!='A':
        sa.append(now)
        now=0
        swo.append(s[i])
    else:
        now+=1
sa.append(now)

now=0
for i in range(len(t)):
    if t[i]!='A':
        ta.append(now)
        now=0
        two.append(t[i])
    else:
        now+=1
ta.append(now)

if swo!=two:
    print(-1)
else:
    ans=0
    for i in range(len(sa)):
        ans+=abs(sa[i]-ta[i])
    print(ans)