
"""
#넘파이 사용 버전. 백준은 넘파이가 사용이 안 된다.
import numpy as np

def division_sol(term, white=0, blue=0):
    size = len(term)
    #항상 정배열을 유지하기 때문에, len이 2 이상이면 2차원 배열 이상이다.
    if size >= 2:
        if(np.allclose(term, term[0])):
            if term[0][0] == 0: blue+=1
            else: white +=1
        else:
            coordinates = [
                (0, size//2, 0, size//2),
                (0, size//2, size//2, size),
                (size//2, size, 0, size//2),
                (size//2, size, size//2, size)
            ]
            for x1, x2, y1, y2 in coordinates:
                x, y = division_sol(term[x1:x2, y1:y2])
                white += x
                blue += y
    else:
        if term[0] == 0: blue+=1
        else: white +=1

    return white,blue

base = []

length = int(input())
for i in range(length):
    base.append(list(map(int,input().split())))

base = np.array(base)
white,blue = division_sol(base)

print (blue)
print (white)
"""

def division_sol(term, white=0, blue=0):
    size = len(term)
    #항상 정배열을 유지하기 때문에, len이 2 이상이면 2차원 배열 이상이다.
    if size >= 2:
        if all(term[i][j] == term[0][0] for i in range(size) for j in range(size)):
            if term[0][0] == 0: 
                blue += 1
            else: 
                white += 1
        else:
            coordinates = [
                (0, size//2, 0, size//2),
                (0, size//2, size//2, size),
                (size//2, size, 0, size//2),
                (size//2, size, size//2, size)
            ]
            for x1, x2, y1, y2 in coordinates:
                sub_term = [row[y1:y2] for row in term[x1:x2]]
                x, y = division_sol(sub_term)
                white += x
                blue += y
    else:
        if term[0][0] == 0: 
            blue += 1
        else: 
            white += 1

    return white, blue

base = []

length = int(input())
for i in range(length):
    base.append(list(map(int, input().split())))

white, blue = division_sol(base)

print(blue)
print(white)