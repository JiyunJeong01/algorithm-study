from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    for i in range (len(prices)):
        now_price = queue.popleft()
        sec = 0
        for j in queue:
            sec +=1
            if (now_price > j):
                break
        answer.append(sec)

    return answer