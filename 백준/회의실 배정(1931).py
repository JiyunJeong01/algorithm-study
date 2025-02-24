N = int(input())

meeting = []
for _ in range(N):
    meeting.append(tuple(map(int,input().split())))

# 회의가 끝나는 순으로 정렬한다. 빨리 끝날수록, 넣기 좋기 때문이다.
meeting.sort(key=lambda x:(x[1],x[0]))

meetingTime = 0
useCount = 0

# 리스트를 돌면서 사용할 수 있을경우 userCount를 추가한다.
for start,end in meeting:
    if (start >= meetingTime):
        meetingTime = end
        useCount +=1

print (useCount)