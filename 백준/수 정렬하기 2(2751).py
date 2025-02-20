import sys

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, equal, rigth = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            rigth.append(num)
        else:
            equal.append(num)
    return QuickSort(left) + equal + QuickSort(rigth)

N = int(sys.stdin.readline())
answer = []

for i in range (N):
    answer.append(int(sys.stdin.readline()))

answer = QuickSort(answer)

for i in answer:
    print (i)