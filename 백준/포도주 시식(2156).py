n = int(input())
grape_list = [0]

for i in range (n):
    grape_list.append(int(input()))

# grape_list는 연속으로 넣지 않는 경우를 저장하고,
# sub_list는 연속으로 넣었을 경우를 저장한다.
sub_list = [0, grape_list[1]]


if ((n+1) > 2):
    for i in range(2, (n+1)):
        # 현재 위치의 값과, 바로 이전의 값을 넣은 경우 / 이번 값을 넣지 않는 경우 중 더 큰 값을 sub_list에 저장한다.
        sub_list.append(max(grape_list[i-1] + grape_list[i], sub_list[i-1]))
        
        # 현재 위치의 값과, 전전 값을 넣은 경우 / 이번 값을 넣지 않는 경우 중 더 큰 값을 grape_list에저장한다.
        # 전전 값을 넣는 경우는, 이전에 연속이 되었어도 상관 없기 때문에 sub_list를 사용한다.
        grape_list[i] = max((grape_list[i] + sub_list[i-2]), sub_list[i-1])
    
print (max(sub_list[n], grape_list[n]))