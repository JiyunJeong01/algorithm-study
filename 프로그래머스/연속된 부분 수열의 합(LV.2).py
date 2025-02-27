# 투포인터 사용
def solution(sequence, k):
    size = len(sequence)
    
    start, end = 0, 0
    current_sum = sequence[0]
    answer = [0, size - 1]
    
    while start < size and end < size:
        if current_sum < k:
            # 합이 부족하면 end를 증가시켜서 구간을 늘림
            end += 1
            if end < size:
                current_sum += sequence[end]
        elif current_sum > k:
            # 합이 넘치면 start를 증가시켜서 구간을 줄임
            current_sum -= sequence[start]
            start += 1
        else:
            # 구간합이 정확히 k인 경우
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            
            # 다음 구간 찾기 위해 start 증가 (현재 구간은 이미 확인했으므로)
            current_sum -= sequence[start]
            start += 1
    
    return answer
