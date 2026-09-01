h,w,k=map(int, input().split())
s=[list(input()) for i in range(h)]
st=[list(i) for i in zip(*s)]

def f(s,h,w): #各列のドットのmin値を返す
    ans=10**18
    for i in range(h):
        d,b=[0]*(w+1),[0]*(w+1)
        for j in range(w):
            d[j+1]=d[j]+(1 if s[i][j]=='.' else 0)
            b[j+1]=b[j]+(1 if s[i][j]=='x' else 0)
        for j in range(w-k+1): #累積和を比べxがないときの.最小値
            if b[j+k]-b[j]==0: 
                ans=min(ans,d[j+k]-d[j])
    return ans

ans=min(f(s,h,w),f(st,w,h)) #列行どっちも
print(ans if ans!=10**18 else -1)