from collections import deque

N, M = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(N)]

direction = [[0,1],
             [0,-1],
             [1,0],
             [-1,0]]

position = []
def bfs(y,x):
    queue = deque()
    queue.append((y,x))

    while queue:
        y1,x1 = queue.popleft()
        for dy, dx in direction:
            if (0<=dy+y1<N and 0<=dx+x1<M):
                if (maze[dy+y1][dx+x1] == 1):
                    maze[dy+y1][dx+x1] += maze[y1][x1]
                    queue.append((dy+y1, dx+x1))

bfs(0,0)
print (maze[N-1][M-1])