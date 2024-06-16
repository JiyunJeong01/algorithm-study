#처음 짠 코드 - 효율성 테스트 1개 실패했다.
"""
def solution(people, limit):
    answer = 0
    people=sorted(people)
    while people:
        count = people.pop()
        if people:
            if (people[0] + count <= limit):
                del people[0]
        answer +=1
    return answer
"""

def solution(people, limit):
    answer = 0
    people=sorted(people)
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람을 다음으로
        right -= 1  # 무거운 사람을 태움
        answer += 1  # 구명보트 사용 횟수 증가
    
    return answer