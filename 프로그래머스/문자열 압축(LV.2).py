def solution(s):
    length2 = len(s)
    answer = length2
    #일정 단위로 나눠본다.
    for length in range (1, (length2//2)+1):
        term_answer = 0
        term = ([s[i:i+length] for i in range(0, len(s), length)])
        start = []
        continuese=False
        count = 1
        
        #연속되는걸 확인한다.
        for i in term:
		        #아무것도 없을 경우(첫번째일 경우 append로 추가)
            if not start:
                start.append(i)
                continue
            
            #만약 연속되지 않은게 왔을 경우, 해당 문자열 추가
            if (start[-1] != i):
                start.append(i)
                count = 1
                continuese = False
            #연속된 게 왔고, 처음으로 연속된 것일 경우, 지정된 위치에 숫자 카운트 추가
            elif (start[-1] == i and continuese == False):
                count +=1
                start.insert(-1,str(count))
                continuese = True
            #연속된 게 왔고, 연속된지 2번재 이상일 경우, 지정된 위치의 숫자 증가
            elif (start[-1] == i and continuese == True):
                count +=1
                start[-2] = str(count)
        
        #정답 길이 출력
        if (len(''.join(start))<answer):
            answer = len(''.join(start))
    

    return answer