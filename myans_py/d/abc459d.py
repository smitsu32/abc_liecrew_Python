for i in range(int(input())):
    s=list(input())
    cnt=[0]*26
    for i in s:
        cnt[ord(i)-ord('a')]+=1
    
    mx,mxi=0,''
    for i in range(26):
        if cnt[i]>mx:
            mx=cnt[i]
            mxi=chr(ord('a')+i)
        
    if mx>(len(s)+1)//2:
        print('No')
    else:
        print('Yes')
        
        ans=['']*len(s)
        j=0
        # cntの降順
        for i in sorted(range(26),key=lambda x:-cnt[x]):
            for _ in range(cnt[i]):
                ans[j]=chr(ord('a')+i)
                if j+2<len(s): #ぐorき
                    j+=2
                else: #末端
                    j=1
        
        # print(*ans,sep='')よりめっちゃはやい
        print(''.join(ans))