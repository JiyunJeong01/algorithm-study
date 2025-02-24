numSize = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

minNum = None
maxNum = None

def is_promising(i):
    if operator[i] >= 1:
        return True
    return False

def solve(count, total):
    global minNum, maxNum
    if count == numSize:
        if (minNum == None or total < minNum):
            minNum = total
        if (maxNum == None or total > maxNum):
            maxNum = total
        return

    for i in range (4):
        if (operator[i] >=1):
            term = total
            operator[i] -=1
            if i == 0:
                total += numbers[count]
            elif i == 1:
                total -= numbers[count]
            elif i == 2:
                total *= numbers[count]
            else:
                if total < 0:
                    total = -(-total // numbers[count])
                else:
                    total //= numbers[count]
            
            solve(count+1, total)
            total = term
            operator[i] +=1

solve(1, numbers[0])
print (maxNum)
print (minNum)