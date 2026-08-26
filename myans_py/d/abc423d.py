from heapq import heappop,heappush

n,k=map(int, input().split())
abc=[list(map(int, input().split())) for i in range(n)]

h=[]
pt,now=0,0 #ループ開始時の時間、人数
for i in range(n):
    a,b,c=abc[i] # t_in,t_stay,cur
    nt=max(pt,a) # 今の時間
    while h and now+c>k:
        tt,cc=heappop(h)
        now-=cc
        nt=max(nt,tt)
    now+=c
    heappush(h,(nt+b,c)) #出る時間、人数
    pt=nt
    print(pt)