# 시간 초과 뜸
"""
numSize, M = map(int,input().split())
numbers = list(map(int,input().split()))

for i in range (M):
    sum = 0
    start, end = map(int, input().split())
    for j in range (start-1, end):
        sum +=numbers[j]
    print (sum)
"""
#누적 합 방식
numSize, M = map(int, input().split())
numbers = list(map(int,input().split()))

sum = [0] * (numSize+1)

for i in range (1, numSize):
    sum[i] = sum[i-1] + numbers[i-1]

for _ in range (M):
    start, end = map(int,input().split())
    result = sum[end] - sum[start-1]
    print (result)