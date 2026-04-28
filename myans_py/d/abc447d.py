s=input()

# 貪欲にaがあるときにbがくれば増やし、現ABセットを記録
nowa,nowb,nowc=0,0,0
for i in range(len(s)):
    if s[i]=='A':
        nowa+=1
    elif s[i]=='B':
        nowb=min(nowa,nowb+1) # bの個数はaのそれを超えてはならず、bは1個くるため
    else:
        nowc=min(nowb,nowc+1)

print(nowc)