def solution(storey):
    answer = 0

    while storey > 0:
        ten = storey % 10  # 마지막 자릿수
        if ten > 5:
            answer += (10 - ten)
            storey = storey // 10 + 1 
        elif ten == 5 and (storey // 10) % 10 >= 5:
            # 다음 자릿수가 5 이상이면 반올림
            answer += (10 - ten)
            storey = storey // 10 + 1
        else:
            answer += ten
            storey //= 10
    
    return answer