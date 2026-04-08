# X:0 1 1 0 0 1 (=3)
# Y:0 1 1 1 1 0 (=4)
# C:0 0 0 1 1 1 (Popcount)
# xorを0(0,0)(1,1)と1(1,0)(0,1)に分割

a,b,c=map(int, input().split())

one=c.bit_count() # (1,0)(0,1)の数
zero=60-one # 2**60 (1,1)(0,0)の数

# (0,1)or(1,0)の数を数える
d=a+b-one 
if d<0 or d%2==1: # (1,1)が負個or(1,1)のみの1が奇数個なら不可能
    print(-1)
    exit()

d//=2
a-=d; b-=d # ここからは(1,1)(0,0)を考える
if d>zero or a<0 or b<0:
    print(-1)
    exit()

x,y=[0]*60,[0]*60 #ans
i0,i1=[],[] #各桁が1か0か

for i in range(60):
    if (c>>i&1): #i桁が1のとき
        i1.append(i)
    else: #0のとき
        i0.append(i)

for i in range(d): #0のときd個(1,1)にする (場所は任意)
    x[i0[i]]=y[i0[i]]=1

for i in range(one): #1のとき先頭a個を(1,0)に、残りb個を(0,1)にする
    if i<a: #前のa個を変える
        x[i1[i]]=1
    else: #後のa個を変える
        y[i1[i]]=1

ax,ay=0,0
for i in range(60):
    if x[i]: ax|=(1<<i) # 2->10
    if y[i]: ay|=(1<<i)
print(ax,ay)