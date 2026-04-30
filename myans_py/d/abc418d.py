n=int(input())
t=input()

ans=0
odd,even=0,0 # 0の個数の偶奇

for i in t:
    if i=='1': # 00 -> 001では単純に偶数の選び方が1通り増える(00,001)
        even+=1
    else: # 0の個数が1増える → 偶奇入れ替え
        odd,even=even,odd
        # 奇数の選び方が増える (a, [a,1])
        odd+=1
    
    ans+=even

print(ans)