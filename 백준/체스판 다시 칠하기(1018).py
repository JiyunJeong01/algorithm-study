
#문제: nxn배열로 된 나무판이 있다. 각 판은 검정색, 또는 하양색으로 칠해져있다.
#이 nxn배열의 나무판에서 8x8의 크기를 잘라 체스판을 만들려고 한다.
#체스판은 흰색이 먼저 시작될 수도, 검은색이 먼저 시작될 수도 있다.
#해당 나무판을 잘랐을 때, 다시 칠해야 하는 수의 최소 수를 구해라.

row, colum = map(int,input().split())

#입력받은 값의 해당 자리가 정답인지 아닌지 1과 0으로 표시하는 배열.
#2개가 있는 이유는 첫번재가 흰색이 올 수도, 검은색이 올 수도 있기 때문.
first_white = []
first_black = []

#입력받은 값과 같은 크기의 2차원 배열 생성
for i in range(row):
    first_white.append([])
    first_black.append([])
    for j in range(colum):
        first_white[i].append(0)
        first_black[i].append(0)

#검사하는 행이 몇번재 행인지 체크 = 홀과 짝의 수마다 첫번째가 검정색인지, 하얀색인지 달라지기 때문.
term_n = 0
for i in range(row):
    board_color = list(input())
		#검사하는 열이 몇번째 열인지 체크 = 흰색과 검은색이 매번 번갈아 나와야하기 때문.
    term_num = 0
		
		#검사하는 칸의 짝,홀수번재 열과 행을 체크하고, 안에 있는 색의 유무 체크 후 값에 따라 알맞은 값 투입.
    for j in range (len(board_color)):
        if board_color[j] == 'B':
            if term_n%2 == 0:
                if term_num%2 == 0:
                    first_white[i][j] = 1
                else:
                    first_black[i][j] = 1
            else:
                if term_num%2 == 0:
                    first_black[i][j] = 1
                else:
                    first_white[i][j] = 1
        else:
            if term_n%2 == 0:
                if term_num%2 == 0:
                    first_black[i][j] = 1
                else:
                    first_white[i][j] = 1
            else:
                if term_num%2 == 0:
                    first_white[i][j] = 1
                else:
                    first_black[i][j] = 1
        term_num +=1
    term_n +=1

#바꿔야 하는 갯수를 알기 위한 알고리즘 구현 부분
#8x8체스판의 최악의 경우는 다 바꿔야 하는 거기 때문에 64 선정.
min = 64

# 한 행의 7개의 값을 sum으로 합치기. 해당 짓을 8번 반복하기.==(인자 값 k)
# 위의 8번 돌린 값을 term 값에 넣어 8x8의 값을 저장.
# 해당 값이 min보다 작으면 대체.
# 위의 행위를 한 행씩 내려가며 반복.
for i in range(row - 7):
    for j in range (colum - 7):
        term = 0
        for k in range(8):
            term += sum(first_black[i+k][0+j:8+j])
        if min > term:
            min = term

        term = 0
        for k in range(8):
            term += sum(first_white[i+k][0+j:8+j])
        if min > term:
            min = term

print (min)