from collections import deque

def solution(progresses, speeds):
    
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while (progresses):
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while (progresses and progresses[0] >= 100):
            progresses.popleft()
            speeds.popleft()
            count +=1
        if (count > 0):
            answer.append(count)

    
    return answer