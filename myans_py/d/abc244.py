s=list(input().split())
t=list(input().split())

c=0
for i in range(3):
    if s[i]==t[i]:
        c+=1

# 1個一致だと不可能(1,3,2  1,2,3  だと1,3,5,...回で一致)
print('Yes' if c!=1 else 'No')