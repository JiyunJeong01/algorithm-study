def binary_search(findN, arr):
    start = 0
    end = len(arr) - 1
    point = (start + end) // 2
    while (start < end and arr[point] != findN):
        if (arr[point] > findN):
            end = point-1
        elif (arr[point] < findN):
            start = point+1
        point = (start + end) // 2
    
    if (arr[point] == findN):
        return 1
    else:
        return 0

N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
X = list(map(int,input().split()))

for num in X:
    print(binary_search(num, A))
