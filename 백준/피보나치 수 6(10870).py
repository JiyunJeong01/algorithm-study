#재귀를 이용해 해결
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)

#DP를 이용해 해결
def Dfibo(n):
    if n < 2:
        return n
    
    if m[n] is None:
        m[n] = Dfibo(n-2) + Dfibo(n-1)
    
    return m[n]

N = int(input())

m = [None] * (N + 1)

print(Dfibo(N))