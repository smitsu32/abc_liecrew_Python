# lca, なんかgcaにも近い？
t=int(input())
for _ in range(t):
    x,y,k=map(int, input().split())
    cnt=0
    # 深い方をrootに近づける→いつか一致する
    while x!=y:
        if x<y:
            y//=k
        else:
            x//=k
        cnt+=1
    print(cnt)