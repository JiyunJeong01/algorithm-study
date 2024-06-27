def solution(N, stages):
    
		#fail_people = 해당 스테이지에 머물러있는 사람 수 (깨는 걸 실패한 사람 수)
		#arri_people = 해당 스테이지까지 도달한 사람 수.
    fail_people=[]
    arri_people=[]
    for _ in range(N):
        fail_people.append(0)
        arri_people.append(0)

		#우선 해당 스테이지에 있는 사람 수를 구함. arri_people은 추가적으로 사용할 것임.
		#인덱스를 넘길 경우 모든 스테이지를 클리어했다는 뜻이므로, 마지막 스테이지에 + 1
    for i in stages:
        try:
            fail_people[i-1] +=1
            arri_people[i-1] +=1
        except IndexError:
            arri_people[-1] +=1
     
		#해당 스테이지에 도달했다는 것은, 그 밑에 있는 스테이지도 전부 도달했었다는 뜻이므로
		#이전 스테이지 도달 값에 현재 스테이지의 값을 넣는 방식을 하향식으로 진행.
		#ex: 4스테이지 도달 값 = 5스테이지 도달 값 + 4스테이지 도달 값 ... 
    for i in range(N-1):
        arri_people[-i-2] +=arri_people[-i-1]
    
		#실패율 기록. 도달한 사람이 없어 산술 오류가 날 경우를 대비해 예외 처리.
    rate = {}
    for i in range(N):
        try:
            rate[i+1] = fail_people[i]/arri_people[i]
        except:
            rate[i+1] = 0
    
		#value값을 기준으로 역순으로 정렬.
    answer = sorted(rate, key=rate.get,reverse=True)
    return answer