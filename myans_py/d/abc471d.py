from heapq import heappop,heappush

q,v=map(int, input().split())
h=[]
for _ in range(q):
    qu=list(map(int, input().split()))
    if qu[0]==1:
        t,w=qu[1:]
        heappush(h,-(w-t)) #最大値のため負
    else:
        t=qu[1]
        if len(h)==0:
            print(-1)
        else:
            print(min(-heappop(h)+t,v))