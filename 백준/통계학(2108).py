#import numpy                   #백준에선 numpy를 사용할 수 없음.BOJ에서는 외부 라이브러리를 불러올 수 없기 때문
from collections import Counter

n = int(input())
numbers = []
for i in range (n):
    numbers.append(int(input()))
numbers.sort()

#반올림해서 평균 구하기
ave = round(sum(numbers)/n)

#중앙값 구하기
if (n % 2 == 0):
    mid = n//2 -1
    meadia = round((numbers[mid] + numbers[(mid+1)])/2)
else:
    mid = n//2
    meadia = round(numbers[mid])

#최빈값 구하기
mode = Counter(numbers).most_common(2)
try:
    if(mode[0][1] == mode[1][1]):   #최빈값이 같다면
        modeN = mode[1][0]          #2번째로 작은 걸 채택
    else:
        modeN = mode[0][0]
except:
    modeN = mode[0][0]

#범위 출력하기
rang = numbers[n-1] - numbers[0]

print(ave)
print(meadia)
print(modeN)
print(rang)

