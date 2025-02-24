def padovan(n):
    if n < 3:
        return 1
    elif n < 5:
        return 2
    
    if not test[n]:
        test[n] = padovan(n-1) + padovan(n-5)
    
    return test[n]


T = int(input())
for i in range(T):
    n = int(input())
    test = [None] * (n+1)
    print(padovan(n-1))