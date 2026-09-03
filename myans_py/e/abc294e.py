# えびまさん解upsolve
l,n1,n2=map(int, input().split())
r1=[list(map(int, input().split())) for i in range(n1)]
r2=[list(map(int, input().split())) for i in range(n2)]
for i in range(1,n1):
    r1[i][1]+=r1[i-1][1] #ﾗﾝレングスを元に戻す
for i in range(1,n2):
    r2[i][1]+=r2[i-1][1]

ans,i,j,c1,c2=0,0,0,0,0
while i<n1 and j<n2:
    if i>0: c1=r1[i-1][1]
    if j>0: c2=r2[j-1][1]
    if r1[i][0]==r2[j][0]:
        ans+=min(r1[i][1],r2[j][1])-max(c1,c2) #今の小さい方のindex-1個前の大きいindex
    
    if r1[i][1]<r2[j][1]:
        i+=1
    else:
        j+=1
print(ans)