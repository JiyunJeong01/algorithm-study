N = int(input())
lost_health = list(map(int,input().split()))
get_happy = list(map(int,input().split()))


dp = [[0] * 101 for i in range(N+1)]
 
for i in range (1, N+1):
    for j in range (1, 101):
        if lost_health[i-1] < j:
            dp[i][j] = max(get_happy[i-1]+dp[i-1][j-lost_health[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print (dp[i][j])