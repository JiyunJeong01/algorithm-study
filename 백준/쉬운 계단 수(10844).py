"""
# 아무리 생각해도 백트래킹으로 푸는 문제가 아닌가? 싶이서 백트래킹으로 풀어본 과정
# 시간초과 뜸
N = int(input())

check = []
answer = 0
def is_promising(num):
    if not check and num == 0:
        return False
    if not check or check[-1]-1 == num  or check[-1]+1 == num :
        return True
    return False

def solve():
    global answer

    if (len(check) == N):
        answer +=1
        return
    
    for i in range (10):
        if (is_promising(i)):
            check.append(i)
            solve()
            check.pop()

solve()
print (answer)

"""

# dp로 풀어보기
N = int(input())
dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if j + 1 <= 9:
            dp[i][j] += dp[i-1][j+1]

answer = sum(dp[N]) % 1000000000

print(answer)
