##解説AC：ふれんずさん
ha,wa=map(int, input().split()); a=[input() for i in range(ha)]
hb,wb=map(int, input().split()); b=[input() for i in range(hb)]
hx,wx=map(int, input().split()); x=[input() for i in range(hx)]

def f(l,ofsi,ofsj): #座標のsetをオフセット込みで返す関数
    bl=set()
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j]=='#':
                bl.add((i+ofsi,j+ofsj))
    return bl

blx=f(x,10,10) #xの黒位置+10を保存..中央に配置

for ai in range(20): #a,bの左上座標で全探索
    for aj in range(20):
        for bi in range(20):
            for bj in range(20):
                blab=f(a,ai,aj)|f(b,bi,bj) #a,bの#の和集合
                if blx==blab:
                    print('Yes')
                    exit()
print('No')