N, M = map(int, input().split())

check = []
def is_promising(num):
    if not check or check[-1] <= num:
        return True
    return False

def solve():
    if (len(check) == M):
        print(*check)
        return
    
    for num in range (1, N+1, 1):
        if (is_promising(num)):
            check.append(num)
            solve()
            check.pop()

solve()