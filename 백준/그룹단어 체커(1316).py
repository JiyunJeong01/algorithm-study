a = int(input())
b = []
for i in range(a):
    b.append(input())

result = 0
for i in b:
    spell = []
    pass2 = True
    for k in i:
        if k in spell:
            try:
                if (spell[spell.index(k)+1] != None):
                    pass2 = False
            except:
                pass
        else:
            spell.append(k)
    if (pass2 == True):
        result +=1

print (result)

"""
#알고리즘 개선본
N = int(input())
a = N

for i in range(N) :
    str = input()

    for j in range(len(str)-1) :
        if (str[j]==str[j+1]) :
            pass
        elif (str[j] in str[j+1:]) :
            a-=1
            break

print(a)
"""