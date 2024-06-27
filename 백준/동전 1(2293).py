n, k = map(int,input().split())
coinL = []
for i in range (n):
    coinL.append(int(input()))
dp = [0 for i in range(k+1)]
dp[0] = 1

for i in coinL:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print (dp[k])