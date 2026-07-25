from itertools import permutations

n=int(input())
p=list(map(int, input().split()))
q=list(map(int, input().split()))

ans=0
for l in list(permutations(range(1,n+1))):
    l=list(l)
    if p<l<q:
        ans+=1

print(ans)