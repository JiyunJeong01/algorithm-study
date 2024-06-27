def solution(book_time):
    #문자열 시간 정수로 변환하는 과정
    bookList = []
    idx = 0
    for i in book_time:
        check = 0 #입실인지 퇴실인지 확인.
        for j in i:
            if check == 0:    #입실시간
                startT=(int(j.replace(":","")))
            else:           #퇴실시간
                endT = (int(j.replace(":","")))
                termM=endT %100//10     #퇴실시간 +10분 청소시간 필요. 만약 50분에 퇴실일 경우 계산.
                if (termM ==5):
                    endT +=50
                else:
                    endT +=10
            check += 1
        book_time[idx] = [startT,endT, 0]
        idx +=1
    
    Llen = len(book_time)
    book_time.sort(key=lambda x:x[1])       #같은 시간에 퇴실처리보다 입실처리가 먼저 일어날 경우 발생하는 오류 방지 정렬
    room = [True for i in range(Llen)]

    for i in range(2359):
        for j in book_time:
            idx = 0
            if i == j[1]:
                room[j[2]] = True
            elif i == j[0]:
                while (room[idx] != True):
                    idx +=1
                j[2] = idx
                room[idx] = False
                
    answer = 0
    for i in book_time:
        answer = max(answer, i[2])
    answer +=1
    
    return answer