count, bag = map(int,input().split())
weightL = []
valueL = []
for i in range (count):
    wT, vT = map(int,input().split())
    weightL.append(wT)
    valueL.append(vT)

dp = [[0] * (bag+1) for i in range(count+1)]
for w in range (1, count+1):
    for v in range (1, bag+1):
        if weightL[w-1] <= v:
            dp[w][v] = max(valueL[w-1]+dp[w-1][v-weightL[w-1]], dp[w-1][v])
        else:
            dp[w][v] = dp[w-1][v]
print (dp[w][v])