# 등비 수열을 이용해서 해결

def solution(word):
    answer = 0
    index = 0
    for i in word:
        if (i == 'A'):
            answer += (5 ** (5-index) // 4 * 0 + 1)
        elif (i == 'E'):
            answer += (5 ** (5-index) // 4 * 1 + 1)
        elif (i == 'I'):
            answer += (5 ** (5-index) // 4 * 2 + 1)
        elif (i == 'O'):
            answer += (5 ** (5-index) // 4 * 3 + 1)
        elif (i == 'U'):
            answer += (5 ** (5-index) // 4 * 4 + 1)
            
        index +=1
    return answer