a,max = map(int, input().split())
num = list(map(int, input().split()))

result = 0
for i in range (a-2):
    sum = 0
    for j in range(a-i-2):
        if (num[i] + num[j+i+1]) < max:
            sum = num[i] + num[j+i+1]
            for k in range (a-j-i-2):
                if (sum + num[k+j+i+2] <= max and sum + num[k+j+i+2] > result):
                    result = sum + num[k+j+i+2]

print (result)