N, M = map(int, input().split())

check = []
def solve():
    if (len(check) == M):
        print(*check)
        return
    
    for num in range (1, N+1, 1):
        check.append(num)
        solve()
        check.pop()

solve()