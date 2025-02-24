# 풀이 생각: -뒤부터 -가 다시 나오기 전까지 전부 괄호로 묶어버리면 되지 않나?
# 알던 주어진 입력을 어떻게 나누지...가 관건.
# -가 한 번이라도 나오는 순간, 모든 수는 다 -연산만 됨

""" 초기에 짠 것
inputMath = input()

termNum = ''
sum = 0
flag = False
for i in inputMath:
    if (i == '+'):
        if flag:
            sum -=int(termNum)
            termNum = ''
            continue
        else:
            sum += int(termNum)
            termNum = ''
            continue
    
    elif (i == '-'):
        if flag:
            sum -=int(termNum)
            termNum = ''
            continue
        else:
            sum += int(termNum)
            flag = True
            termNum = ''
            continue
    termNum +=i

if flag:
    sum -=int(termNum)
else:
    sum +=int(termNum)
print (sum)
"""

inputMath = input()

termNum = ''
sum = 0
flag = False
for i in inputMath:
    if (i == "+" or i =='-'):
        if flag:
            sum -= int(termNum)
        else:
            sum += int(termNum)
        termNum =''
        
        if (i =='-'):
            flag = True
    else:
        termNum += i

if flag:
    sum -=int(termNum)
else:
    sum +=int(termNum)
print (sum)