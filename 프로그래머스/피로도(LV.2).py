from itertools import permutations

def solution(k, dungeons):
    perList = list(permutations(dungeons, len(dungeons)))
    
    answer = -1
    for i in perList:
        count = 0
        termH = k
        for j in i:
            if j[0]<=termH:
                count +=1
                termH -= j[1]
        if (answer < count):
            answer = count
    return answer