import itertools

def solution(numbers):
    answer = 0
    com = []
    
    #순회를 돌아서 경우의 수 모두 구하기
    for i in range (1, len(numbers)+1):
        nPr = itertools.permutations(numbers, i)
        
        for j in nPr:
            com.append(''.join(j))
    
    #str int형으로 변환
    for i in range (len(com)):
        com[i] = int(com[i])
    #중복 삭제하기&0,1 삭제하기
    com = set(com)
    com = list(com)
    try:
        com.remove(0)
    except:
        print("gg")
    try:
        com.remove(1)
    except:
        print("gg")
    
    #소수인지 확인
    for i in com:
        check = True
        for j in range(2, i):
            if (i % j ==0):
                check = False
                break
        if (check == True):
            answer +=1
    return answer