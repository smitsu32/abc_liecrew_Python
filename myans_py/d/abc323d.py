from collections import defaultdict

n=int(input())
d=defaultdict(int)
for i in range(n):
    s,c=map(int, input().split())
    di=0
    while s%2==0: #同じ奇数なら2**diで重複処理になるため
        s//=2
        di+=1
    d[s]+=c*2**di

ans=0
for i in d.values():
    ans+=i.bit_count() # 5->111で3個になる
print(ans)