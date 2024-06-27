from collections import Counter

def solution(weights):
    answer = 0
    
    #중복이면 무조건 균형을 맞출 수 있으므로 중복 경우 세기
    temp = Counter(weights)
    for i in temp:
        if (temp[i] >=2):
            answer += temp[i] * (temp[i]-1) //2

    #중복 경우 다 셌으면 중복 삭제
    weights = set(weights)
    
    #실제로 계산하기
    for i in (weights):
        if i*2/3 in weights:
            answer+= temp[i] * temp[i*2/3]
        if i*2/4 in weights:
            answer += temp[i] * temp[i*2/4]
        if i*3/4 in weights:
            answer += temp[i] * temp[i*3/4]
            
    return answer