import operator

N, M = map(int,input().split())

check = {}
for _ in range (N):
    word = input()
    if (len(word) >= M):
        if (word in check):
            check[word] +=1
        else:
            check[word] = 1
    
check = sorted(check.items(), key=operator.itemgetter(1), reverse=True)

for i, _ in check:  
    print(i)