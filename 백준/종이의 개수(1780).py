
answer =[0,0,0]

def check_equal(value, arr):
    for i in arr:
        for j in i:
            if j != value:
                return False
    return True

def solve(paper, N):
    global answer

    first_value = paper[0][0]
    if (N >=2):
        if check_equal(first_value, paper):
            if first_value == -1:
                answer[0] +=1
            elif first_value == 0:
                answer[1] +=1
            else:
                answer[2] +=1

        else:
            coordinates = [
                (0, N//3, 0, N//3),
                (0, N//3, N//3, N//3*2),
                (0, N//3, N//3*2, N),

                (N//3, N//3*2, 0, N//3),
                (N//3, N//3*2, N//3, N//3*2),
                (N//3, N//3*2, N//3*2, N),

                (N//3*2, N, 0, N//3),
                (N//3*2, N, N//3, N//3*2),
                (N//3*2, N, N//3*2, N),
            ]
            for x1, x2, y1, y2 in coordinates:
                sum_term = [row[y1:y2] for row in paper[x1:x2]]
                solve(sum_term, N//3)
    else:
        if first_value == -1:
            answer[0] +=1
        elif first_value == 0:
            answer[1] +=1
        else:
            answer[2] +=1

N = int(input())
paper = []
for _ in range (N):
    paper.append(list(map(int,input().split())))

solve(paper, N)
print(answer)