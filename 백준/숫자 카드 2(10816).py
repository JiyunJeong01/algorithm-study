from collections import Counter

N = int(input())
CardList = list(map(int, input().split()))
M = int(input())
SearchList = list(map(int,input().split()))
answer = [0 for i in range (M)]

CardList = Counter(CardList)
CardNum = sorted(CardList)

index2 = 0
for i in SearchList:
    start = 0
    end = len(CardNum)-1
    while start <=end:
        mid = (start + end) //2
        if (CardNum[mid] == i):
            answer[index2] +=CardList[CardNum[mid]]
            break
        elif (CardNum[mid] > i):
            end = mid-1
        elif (CardNum[mid] < i):
            start = mid +1
    index2 +=1

print (*answer)