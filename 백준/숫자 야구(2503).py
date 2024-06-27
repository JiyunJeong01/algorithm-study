import sys
from itertools import permutations

n = int(input())

#가능한 경우의 수 만들어주는 함수.
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

#해결법= 입력 받은 값을 토대로, 스트라이크와 볼의 갯수가 똑같이 나오는 경우의 수만 남기고 나머지는 다 삭제하는 알고리즘.
#예를 들어 486 1 1 이라면, 똑같이 해당 숫자를 기반으로 ball 1 strike 1이 나오는 경우의 숫자들 제외하곤 전부 삭제.
for _ in range(n):
    test, s, b = map(int, input().split())
    test = list(str(test))
    remove_cnt = 0

		#현재 이용 가능한 
    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= remove_cnt

				#각 입력받은 test 자리수에 대한 반복문 진행.
        for j in range(3):
            test[j] = int(test[j])

						#만약 입력받은 값이 num이라는 경우의 수 안에 존재 한다면
            if test[j] in num[i]:
								#게다가 자리까지 똑같다면? strike count 증가.
                if j == num[i].index(test[j]):
                    s_cnt += 1
								#자리가 똑같진 않고 존재만 한다면 ball count 증가
                else:
                    b_cnt += 1
		    
				#위의 순회를 돌았을때, 스트라이크 수와 볼 수가 같은지 확인. 아니라면 틀린 경우이므로 삭제.
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_cnt += 1

print(len(num))