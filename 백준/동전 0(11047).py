N, K = map(int, input().split())

coins = []

for _ in range (N):
    coins.append(int(input()))

# reverse 하는 것보다 for문에서 거꾸로 올라가는게 더 나을 수도
count = 0
for i in range (N-1, -1, -1):
    if (K == 0):
        break
    if (coins[i] <= K):
        count += (K//coins[i])
        K %= coins[i]

print (count)