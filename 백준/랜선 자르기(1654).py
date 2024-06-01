k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

low = 1  # 최소 길이는 1로 설정합니다.
high = max(lines)  # 최대 길이는 가장 긴 선의 길이로 설정합니다.

while low <= high:
    mid = (low + high) // 2
    count = 0
    
    # mid 길이로 몇 개의 조각을 만들 수 있는지 계산
    for line in lines:
        count += line // mid
    
    if count >= n:
        low = mid + 1  # 더 긴 길이를 찾기 위해 범위를 위로 조정합니다.
    else:
        high = mid - 1  # 더 짧은 길이를 찾기 위해 범위를 아래로 조정합니다.

print(high)  # 최종적으로 최대 길이를 출력합니다.