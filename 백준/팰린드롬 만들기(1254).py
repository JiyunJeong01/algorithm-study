from collections import deque

text = list(input())
size = len(text)

for i in range (size):
    front = text[i]
    back = text[-(i+1)]

    term = list(reversed(text))
    
    #검사하는 문자열이 같더라도, 전체적으로 회문이 아닐 경우에는 요구하는 경우에 부합하지 않으므로 문자 추가 
    if (front != back or term != text):
        text.insert(size, front)

print (len(text))