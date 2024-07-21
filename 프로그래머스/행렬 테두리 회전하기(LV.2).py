def solution(rows, columns, queries):
    arr = [[j+1+(i*columns) for j in range(columns)] for i in range(rows)]
    answer = []
    for y,x,b,a in queries:
        min = arr[y-1][x-1]

        #맨윗줄(오른쪽으로가기)
        for j in range(x-1,a-1):
            term = arr[y-1][j+1]
            arr[y-1][j+1] = arr[y-1][x-1]
            arr[y-1][x-1] = term
            if (term < min):
                min = term

        #오른쪽줄(내려가기)
        for j in range(y-1, b-1):
            term = arr[j+1][a-1]
            arr[j+1][a-1] = arr[y-1][x-1]
            arr[y-1][x-1] = term
            if (term < min):
                min = term

        #맨아랫줄(왼쪽으로가기)
        for j in range(a-1,x-1,-1):
            term = arr[b-1][j-1]
            arr[b-1][j-1] = arr[y-1][x-1]
            arr[y-1][x-1] = term
            if (term < min):
                min = term

        #왼쪽줄(올라가기)
        for j in range(b-1, y-1, -1):
            term = arr[j-1][x-1]
            arr[j-1][x-1] = arr[y-1][x-1]
            arr[y-1][x-1] = term
            if (term < min):
                min = term
        answer.append(min)
    return answer