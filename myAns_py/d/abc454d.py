n=int(input())
xx=['(','x','x',')']

def f(a):
    la=[]
    for i in a:
        la.append(i)
        if len(la)>=4 and la[-4:]==xx:
            del la[-1],la[-3] # approximate O(1)
    return la

for _ in range(n):
    a=input()
    b=input()
    
    if f(a)==f(b):
        print('Yes')
    else:
        print('No')