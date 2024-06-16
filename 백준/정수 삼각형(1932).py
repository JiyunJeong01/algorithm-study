#처음 제출한 코드 - 시간 초과
"""
import sys

def dfs(all_list, length, depth_index, index, current_sum):
    if (depth_index == length): return current_sum
    else:
        return max(dfs(all_list,length, depth_index + 1,index,current_sum + all_list[depth_index][index]), dfs(all_list,length, depth_index + 1,index + 1,current_sum + all_list[depth_index][index]))



n = int(sys.stdin.readline())
list2 = []
for i in range (n):
    list2.append(list(map(int,sys.stdin.readline().split())))

print((dfs(list2, n, 0, 0, 0)))
"""

n = int(input())
list2 = []
for i in range (n):
    list2.append(list(map(int,input().split())))

for i in range (1, n):
    for j in range (len(list2[i])):
        if (j ==0):
            list2[i][j] = list2[i][j] + list2[i-1][j]
        elif (j == len(list2[i]) -1):
            list2[i][j] = list2[i][j] + list2[i-1][j-1]
        else:
            list2[i][j] = max(list2[i][j] + list2[i-1][j],list2[i][j] + list2[i-1][j-1])

print (max(list2[n-1]))