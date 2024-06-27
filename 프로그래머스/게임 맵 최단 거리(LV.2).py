#미로가 주어졌을 때 해당 미로를 탈출하는 최소 값을 구하라.

from collections import deque


def solution(maps):
    # 맵 넓이 지정
    map_width = len(maps)
    map_height = len(maps[0])
    
    # 방문했는지 확인하는 노드 지정
    visited = [[0 for j in range(map_height)] for i in range(map_width)]
    visited[0][0] = 1
    
    # 현재 위치에서 방문할 수 있는 노드 deque에 지정
    queue = deque()
		# 첫 시작은 0, 0 좌표
    queue.append([0,0])
    
    # 좌표 이동을 알려주는 표식
    mx = [1,-1,0,0]
    my = [0,0,1,-1]
    
    answer = -1
    
    # 너비 우선 탐색 응용
    while queue:
				#탐색할 수 있는 좌표를 하나 pop함.
        x,y = queue.popleft()
        
        # 목적지에 도달했을 경우
        if (x == map_width-1 and y == map_height-1):
            answer = visited[x][y]
        
        # 너비 우선 탐색을 위해 상하좌우를 먼저 탐색하는 bfs 알고리즘 실행
        for i in range(4):
            term_x = mx[i] + x
            term_y = my[i] + y

            #이동한 위치가 맵에 있는지 확인
            if (0  <= term_x < map_width and 0 <= term_y < map_height):
                #이동한 위치가 벽에 막혀있지 않는지 확인
                if ((maps[term_x][term_y]) == 1):
                    #이동한 위치가 방문한 적 있는지 확인
                    if ((visited[term_x][term_y] == 0)):
                        visited[term_x][term_y] = visited[x][y] + 1
                        queue.append([term_x, term_y])
    return answer