from collections import deque

def searchmap(y,x, maps, ySize, xSize):
    
    direction = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0)
    ]
    
    queue = deque()
    queue.append((y,x))
    
    result = int(maps[y][x])
    maps[y][x] = "X"
    
    while queue:
        y,x = queue.popleft()
        
        for dirY, dirX in direction:
            if (0 <= (dirY+y) < ySize and 0 <= (dirX +x) < xSize):
                if (maps[dirY+y][dirX+x] != "X"):
                    queue.append((dirY+y, dirX+x))
                    result += int(maps[dirY+y][dirX+x])
                    maps[dirY+y][dirX+x] = "X"
    return result

def solution(maps):
    answer = []
    
    xSize = len(maps[0])
    ySize = len(maps)
    
    # 리스트로 변경
    # 차후 대체할때, str은 대체가 안되기 때문에 리스트로 변경함.
    for i in range(ySize):
        maps[i] = list(maps[i])
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (maps[i][j] == "X"):
                continue
            else:
                answer.append(searchmap(i,j, maps, ySize, xSize))
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)
        
    return answer