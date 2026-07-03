t=int(input())
for i in range(t):
    n,w=map(int, input().split())
    c=list(map(int, input().split()))
    
    l=[0]*(2*w) # cのコストを周期2*Wごとに合算
    for i in range(n):
        l[i%(2*w)]+=c[i]
    l+=l #尺取りのため2倍に

    cur=sum(l[:w])
    ans=cur
    # 幅2*wをずらしていく
    for i in range(2*w-1):
        cur+=l[i+w]-l[i]
        ans=min(ans,cur)
    
    print(ans)