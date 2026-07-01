h,w,q=map(int, input().split())
rcx=[]
for _ in range(q):
    r,c,x=input().split()
    rcx.append([int(r),int(c),x])

g=[['A']*w for _ in range(h)]
mc=[0]*h
for r,c,x in reversed(rcx):
    for i in range(r-1,-1,-1):
        if mc[i]>=c: break #既に塗られているとき
        for j in range(mc[i],c): # 更新前の各マスを上書き
            g[i][j]=x
        mc[i]=c # c列以上は決定済み

for i in g:
    print(''.join(i))