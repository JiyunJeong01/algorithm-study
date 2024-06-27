a = input()
a = a.upper()
dic = {}
for i in a:
    if (i in dic):
        dic[i] +=1
    else:
        dic[i] = 1

max = 0
max_spell = 0
for i in dic:
    if (dic[i] > max):
        max = dic[i]
        max_spell = i
    elif (max == dic[i]):
        max_spell = "?"

print (max_spell)