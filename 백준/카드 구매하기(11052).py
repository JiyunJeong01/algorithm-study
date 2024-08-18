n = int(input())
price = list(map(int,input().split()))
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+1, n+1):
        dp[j] = max(dp[j-(i+1)]+price[i],dp[j])
        print(dp)

print (dp[n])