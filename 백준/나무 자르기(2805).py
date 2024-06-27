N, M = (map(int, input().split()))
height = list(map(int,input().split()))

height.sort(reverse=True)
height.append(0)
tree_max = max(height)

index = 0
treeSum = 0
result = tree_max

for i in range(tree_max):
    while (result == height[index]):
        index +=1
    treeSum += (index)
    result -=1
    if (treeSum >= M):
        break

print (result)

"""
#이분탐색을 사용한 알고리즘 해결법

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
"""