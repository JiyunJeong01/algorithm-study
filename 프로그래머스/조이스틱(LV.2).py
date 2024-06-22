def solution(name):
    answer = 0
    # 이동할 때 최악의 경우는 한방향으로만 갔을 경우
    move = len(name) - 1
    for i in range(len(name)):
        # 현재 위치의 값 맞추기
        answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)
        
        # 다음으로 이동할 위치 찾기
        # left = 왼쪽 끝에서, 현재 위치까지 움직인 거리
        left = i
        idx = left + 1
        while (idx < len(name)) and (name[idx] == 'A'):
            idx += 1
        # right = 오른쪽 끝에서 left 오른쪽을 기준으로 처음으로 A가 아닌 알파벳 까지의 거리
        right = len(name) - idx
        # 오른쪽에서 출발하는 것과 왼쪽에서 출발하는 것 중 더 작은 거리를 갔다가 되돌아 온다.
        back_distance = min(left, right)
        move = min(move, left + right + back_distance)
        print (left, right, move)
        
    answer += move
    return answer