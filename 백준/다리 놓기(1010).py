N = int(input())

def factorial (n):
    result = 1
    for i in range (2, n+1, 1):
        result *=i

    return result

for _ in range (N):
    left, right = map(int, input().split())

    result = factorial(right) // (factorial(left) * (factorial(right-left)))
    
    print (result)
    