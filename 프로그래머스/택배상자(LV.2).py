from collections import deque

def solution(order):
    length = len(order)
    container = []
    for i in range(length):
        container.append(i+1)
    
    container = deque(container)
    second_con = []
    count = 0
    high = 0
    save = 0
    
    for i in order:
        save +=1
        
        if i > high:
            high = i
            for j in range(length):
                term = container.popleft()
                if term == i:
                    count +=1
                    break
                else:
                    second_con.append(term)
                    
        else:
            if second_con[-1] == i:
                second_con.pop()
                count +=1
        
        if save != count:
            break
            
    return count