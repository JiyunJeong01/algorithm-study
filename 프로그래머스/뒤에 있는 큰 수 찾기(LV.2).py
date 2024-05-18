"""
#시간초과 발생한 코드
def solution(numbers):
    answer = []
    for i in range (len(numbers)):
        maxN = -1
        for j in range(i+1,len(numbers)):
            if (numbers[i] < numbers[j]):
                maxN = numbers[j]
                break
        answer.append(maxN)
    return answer
"""

#스택을 이용하여 시간복잡도 개선
#큰 수를 구할 때, 만약 [6,5,3,2,7] 일 경우, 6 5뒤에 있는 3과 2는 5보다 작기 때문에 필수적으로 고려대상이 될 필요가 없다는 점에서 착안하였다.
def solution(numbers):
    answer = []
    check = [-1]
    maxN = 0
    #거꾸로 올라가며 스택에 값을 넣는다.
    for i in range (len(numbers)-1, -1, -1):
        while (1):
            #스택 최상단에 있는 값(가장 가까운 값)을 가져온다.
            #최상단 값이 현재 값보다 높거나, -1이 될 때까지 스택에서 빼내오는 걸 반복한다.
            maxN = check.pop()
            if (maxN > numbers[i]):
                break
            elif (maxN == -1):
                break
        #최상단 값을 구했으면, 해당 값을 정답란에 넣는다.
        #추 후 다시 사용될 값이기 때문에, maxN을 다시 집어넣고, numbers[i]도 포함한다.
        check.append(maxN)
        check.append(numbers[i])
        answer.append(maxN)
        
    answer.reverse()
    return answer