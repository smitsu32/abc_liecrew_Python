for _ in range(int(input())):
    n=int(input())
    s='0'+input()
    
    f=[False]*2**n
    f[0]=True
    for bit in range(2**n):
        if f[bit]:
            for i in range(n):
                if not bit&1<<i and s[bit+2**i]=='0': # bit==s[nxt]==0のとき
                    f[bit+2**i]=True
    print('Yes' if f[-1] else 'No')