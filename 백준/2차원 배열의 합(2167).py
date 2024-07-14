N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range (1, N+1):
    for j in range (1, M+1):
        dp [i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

K = int(input())

for _ in range (K):
    term_arr = list(map(int, input().split()))
    i = term_arr[0]
    j = term_arr[1]
    x = term_arr[2]
    y = term_arr[3]
    print(dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])